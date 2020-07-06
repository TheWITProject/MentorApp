from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins

from .models import Endpoint
from .serializers import EndpointSerializer

from .models import MLAlgorithm
from .serializers import MLAlgorithmSerializer

from .models import MLAlgorithmStatus
from .serializers import MLAlgorithmStatusSerializer

from .models import MLRequest
from .serializers import MLRequestSerializer

import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response
from ml.registry import MLRegistry
from mentorapp.wsgi import registry

#MIXINS: The mixin classes provide the actions that are used to provide the basic view behavior.
# Note that the mixin classes provide action methods rather than defining the handler methods,
# such as .get() and .post(), directly. This allows for more flexible composition of behavior.

#LISTMODEMIXIN:Provides a .list(request, *args, **kwargs) method, that implements listing a queryset.
# If the queryset is populated, this returns a 200 OK response,
# with a serialized representation of the queryset as the body of the response.
# The response data may optionally be paginated.

#RETRIEVEMODELMIXIN: Provides a .retrieve(request, *args, **kwargs) method, that implements returning an existing model instance in a response.
# If an object can be retrieved this returns a 200 OK response, with a serialized representation of the object as the body of the response.
#  Otherwise it will return a 404 Not Found.

#CREATEMODELMIXIN: Provides a .create(request, *args, **kwargs) method, that implements creating and saving a new model instance.
#If an object is created this returns a 201 Created response, with a serialized representation of the object as the body of the response.
#If the representation contains a key named url, then the Location header of the response will be populated with that value.
#If the request data provided for creating the object was invalid, a 400 Bad Request response will be returned, with the error details as the body of the response.

#UPDATEMODELMIXIN: Provides a .update(request, *args, **kwargs) method, that implements updating and saving an existing model instance.
# Also provides a .partial_update(request, *args, **kwargs) method, which is similar to the update method, except that all fields for the update will be optional.
# This allows support for HTTP PATCH requests.
# If an object is updated this returns a 200 OK response, with a serialized representation of the object as the body of the response.
# If the request data provided for updating the object was invalid, a 400 Bad Request response will be returned, with the error details as the body of the response.

#GENERICVIEWSET: The GenericViewSet class inherits from GenericAPIView, and provides the default set of get_object, get_queryset methods and other generic view base behavior,
#but does not include any actions by default.

# ViewSets use a Serializer or Serializers to correctly represent API-related objects, and are exposed in urls.py by being 
# registered with a Router. API actions provided by a ViewSet include “list”, “create”, “retreive”, “update”, “partial_update”,
#  and “destroy”.
class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = MLAlgorithmStatus.objects.filter(parent_mlalgorithm = instance.parent_mlalgorithm,
                                                        created_at__lt=instance.created_at,
                                                        active=True)
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])

class MLAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False for other statuses
                deactivate_other_statuses(instance)



        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(  #A DRF ViewSet is a collection of views representing all API actions available at an API endpoint
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

class PredictView(views.APIView):
    def post(self, request, endpoint_name, format=None):

        algorithm_status = self.request.query_params.get("status", "production")
        algorithm_version = self.request.query_params.get("version")

        algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, status__status = algorithm_status, status__active=True)
        
        if algorithm_version is not None:
            algs = algs.filter(version = algorithm_version)

        if len(algs) == 0:
            return Response(
                {"status": "Error", "message": "ML algorithm is not available"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(algs) != 1 and algorithm_status != "ab_testing":
            return Response(
                {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        alg_index = 0
        if algorithm_status == "ab_testing":
            alg_index = 0 if rand() < 0.5 else 1

        algorithm_object = registry.endpoints[algs[alg_index].id]
        prediction = algorithm_object.compute_prediction(request.data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=json.dumps(request.data),
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()

        prediction["request_id"] = ml_request.id

        return Response(prediction)
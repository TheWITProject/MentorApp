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

#GENERICVIEWSET: The GenericViewSet class inherits from GenericAPIView, and provides the default set of get_object, get_queryset methods and other generic view base behavior,
#but does not include any actions by default.
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

class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

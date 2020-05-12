from rest_framework import serializers #library to use serializers which contain all the fields
from .models import Endpoint
from .models import MLAlgorithmStatus
from .models import MLAlgorithm
from .models import MLRequest

# Serializers allow complex data such as querysets and model instances to be converted
# to native Python datatypes that can then be easily rendered into JSON, XML or other
#  content types. Serializers also provide deserialization, allowing parsed data to be
#  converted back into complex types, after first validating the incoming data.

# The ModelSerializer class provides a shortcut that lets you automatically create a Serializer
#  class with fields that correspond to the Model fields.
# The ModelSerializer class is the same as a regular Serializer class, except that:
    # It will automatically generate a set of fields for you, based on the model.
    # It will automatically generate validators for the serializer, such as unique_together validators.
    # It includes simple default implementations of .create() and .update().
#Need different serializers because they return different JSON fields. 
class EndpointSerializer(serializers.ModelSerializer):
    class Meta: # Class use to pass extra infomation and it is used in forms.
        model = Endpoint
        read_only_fields = ("id", "name", "created_at") #Read only is to ensure that the field is used when serializing a representation, but is not used when creating or updating an instance during deserialization.
        fields = read_only_fields


class MLAlgorithmSerializer(serializers.ModelSerializer):

    current_status = serializers.SerializerMethodField(read_only=True) # Set to True to ensure the field is used when serializing a representation

    def get_current_status(self, mlalgorithm):
        return MLAlgorithmStatus.objects.filter(parent_mlalgorithm=mlalgorithm).latest('created_at').status

    class Meta:
        model = MLAlgorithm
        read_only_fields = ("id", "name", "code",
                            "created_at",
                            "parent_endpoint", "current_status")
        fields = read_only_fields

class MLAlgorithmStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLAlgorithmStatus
        read_only_fields = ("id", "active")
        fields = ("id", "active", "status", "created_by", "created_at",
                            "parent_mlalgorithm")
        #fields status, created_by, created_at and parent_mlalgorithm are in read and write mode,
        # we will use the to set algorithm status by REST API
class MLRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLRequest
        read_only_fields = (
            "id",
            "input_data",
            "full_response",
            "response",
            "created_at",
            "parent_mlalgorithm",
        )
        fields =  (
            "id",
            "input_data",
            "full_response",
            "response",
            "feedback", #left in read and write mode - needed to provide feedback about match to the server
            "created_at",
            "parent_mlalgorithm",
        )

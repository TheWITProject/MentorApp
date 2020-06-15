from rest_framework import serializers
from .models import Matches


class MatchesSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Matches.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.match_id = validated_data.get('match_id', instance.match_id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance
    class Meta:
        model = Matches
        fields = ("user_id","match_id")

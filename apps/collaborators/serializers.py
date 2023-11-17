from rest_framework import serializers
from .models import Collaborator


class CollaboratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = "__all__"

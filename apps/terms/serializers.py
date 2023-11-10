from rest_framework import serializers
from .models import Terms


class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        exclude = ("id",)

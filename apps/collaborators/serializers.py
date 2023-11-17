from rest_framework import serializers
from .models import Collaborator


class CollaboratorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if (self.context["request"].method == "GET" and
                "list" in self.context["request"].resolver_match.url_name):
            data["total"] = Collaborator.objects.count()

            page_size = self.context["request"].query_params.get("page_size", 10)
            data["total_page"] = (data["total"] + int(page_size) - 1) // int(page_size)

        return data

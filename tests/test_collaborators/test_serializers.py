import pytest
from apps.collaborators.serializers import CollaboratorsSerializer

pytestmark = pytest.mark.django_db


def test_user_serializer(collaborator):
    serializer = CollaboratorsSerializer(instance=collaborator)
    assert serializer.data == {
        "id": collaborator.id,
        "name": collaborator.name,
        "age": collaborator.age,
        "gender": collaborator.gender,
        "role": collaborator.role,
        "salary": collaborator.salary,
        "active": collaborator.active
    }


def test_collaborator_serializer_without_required_fields():
    incomplete_data = {
        "name": "test",
        "age": 20
    }
    serializer = CollaboratorsSerializer(data=incomplete_data)
    assert not serializer.is_valid()


def test_collaborator_serializer_create(collaborator_payload):
    serializer = CollaboratorsSerializer(data=collaborator_payload)
    assert serializer.is_valid()
    validated_data = serializer.validated_data
    collaborator = serializer.create(validated_data)

    assert collaborator.id


def test_partial_update_collaborator_serializer(collaborator):
    old_name = collaborator.name
    serializer = CollaboratorsSerializer(instance=collaborator, data={"name": "new_name"}, partial=True)
    serializer.is_valid(raise_exception=True)
    updated_collaborator = serializer.save()

    assert updated_collaborator.id == collaborator.id
    assert updated_collaborator.name != old_name

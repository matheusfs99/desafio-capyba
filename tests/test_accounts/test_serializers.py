import pytest
from apps.accounts.serializers import UserSerializer

pytestmark = pytest.mark.django_db


def test_user_serializer(user):
    serializer = UserSerializer(instance=user)
    assert serializer.data == {
        "id": user.id,
        "email": user.email,
        "username": user.username,
        "photo": user.photo,
        "password": user.password
    }


def test_user_serializer_without_required_fields():
    incomplete_data = {
        "email": "test@example.com",
        "password": "testpassword"
    }
    serializer = UserSerializer(data=incomplete_data)
    assert not serializer.is_valid()


def test_user_serializer_without_password():
    no_password_data = {
        "email": "test@example.com",
        "username": "testuser",
        "photo": None
    }
    serializer = UserSerializer(data=no_password_data)
    assert not serializer.is_valid()


def test_user_serializer_with_invalid_email():
    invalid_email_data = {
        "email": "invalidemail",
        "username": "testuser",
        "password": "testpassword"
    }
    serializer = UserSerializer(data=invalid_email_data)
    assert not serializer.is_valid()


def test_user_serializer_create(user_payload):
    serializer = UserSerializer(data=user_payload)
    assert serializer.is_valid()
    validated_data = serializer.validated_data
    user = serializer.create(validated_data)

    assert user.id


def test_partial_update_user_serializer(user):
    old_username = user.username
    serializer = UserSerializer(instance=user, data={"username": "new_username"}, partial=True)
    serializer.is_valid(raise_exception=True)
    updated_user = serializer.save()

    assert updated_user.id == user.id
    assert updated_user.username != old_username

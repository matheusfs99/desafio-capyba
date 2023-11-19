import factory
from apps.accounts.models import User


class UserFactory(factory.Factory):
    email = "email@test.com"
    username = "test"
    password = "password123"
    photo = None

    class Meta:
        model = User

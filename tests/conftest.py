import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from tests.factories.accounts import UserFactory
from tests.factories.collaborators import CollaboratorFactory
from tests.factories.terms import TermsFactory

register(UserFactory)
register(CollaboratorFactory)
register(TermsFactory)


@pytest.fixture
def api_client(user):
    user.validated = True
    client = APIClient()
    client.force_authenticate(user)
    return client

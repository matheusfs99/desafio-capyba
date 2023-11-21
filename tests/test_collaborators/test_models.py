import pytest

pytestmark = pytest.mark.django_db


def test_simple_user(collaborator):
    assert collaborator
    assert isinstance(collaborator.name, str)

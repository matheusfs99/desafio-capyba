import pytest

pytestmark = pytest.mark.django_db


def test_simple_user(user):
    assert user
    assert isinstance(user.email, str)


def test_get_full_name(user):
    user.first_name = "Matheus"
    user.last_name = "Farias"
    assert user.get_full_name() == "Matheus Farias"


def test_get_short_name(user):
    user.first_name = "Matheus"
    user.last_name = "Farias"
    assert user.get_short_name() == "Matheus"


def test_validate_user(user):
    assert not user.validated
    user.validate_user()
    assert user.validated


def test_validate_user_validated(user):
    user.validated = True
    assert user.validated
    user.validate_user()
    assert user.validated

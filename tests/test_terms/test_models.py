import pytest

pytestmark = pytest.mark.django_db


def test_simple_term(terms):
    assert terms

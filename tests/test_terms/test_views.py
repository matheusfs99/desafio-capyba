import json
from http import HTTPStatus
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from pytest_factoryboy.fixture import register
from tests.factories.terms import TermsFactory
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db

register(TermsFactory, "another_terms")


def create_terms(terms_factory, amount=1):
    for _ in range(amount):
        terms_factory().save()


def test_list_terms(api_client, terms_factory):
    create_terms(terms_factory, 2)
    url = reverse("terms-list")
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["results"]) == 2


def test_detail_terms(api_client, terms):
    terms.save()
    url = reverse("terms-detail", kwargs={"pk": terms.id})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_terms_nonexistent(api_client):
    url = reverse("terms-detail", kwargs={"pk": 123})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND

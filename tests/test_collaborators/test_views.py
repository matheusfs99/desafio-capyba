import json
from http import HTTPStatus
import pytest
from pytest_factoryboy.fixture import register
from tests.factories.collaborators import CollaboratorFactory
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db

register(CollaboratorFactory, "another_collaborator")


def create_collaborator(collaborator_factory, amount=1):
    for _ in range(amount):
        collaborator_factory().save()


def test_list_collaborators(api_client, collaborator_factory):
    create_collaborator(collaborator_factory, 2)
    url = reverse("collaborator-list")
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK
    assert len(response.json()["results"]) == 2


def test_create_collaborator(api_client, collaborator_payload):
    url = reverse("collaborator-list")
    response = api_client.post(url, collaborator_payload)
    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.parametrize(
    "field", ["name", "age", "gender", "role", "salary"]
)
def test_create_collaborator_without_field(field, api_client, collaborator_payload):
    collaborator_payload.pop(field)
    url = reverse("collaborator-list")
    response = api_client.post(url, collaborator_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize(
    "field", ["name", "age", "gender", "role", "salary"]
)
def test_create_collaborator_with_field_blank(field, api_client, collaborator_payload):
    collaborator_payload[field] = ""
    url = reverse("collaborator-list")
    response = api_client.post(url, collaborator_payload)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_detail_collaborator(api_client, collaborator):
    collaborator.save()
    url = reverse("collaborator-detail", kwargs={"pk": collaborator.id})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_detail_collaborator_nonexistent(api_client):
    url = reverse("collaborator-detail", kwargs={"pk": 123})
    response = api_client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_update_collaborator(api_client, collaborator):
    collaborator.save()
    url = reverse("collaborator-detail", kwargs={"pk": collaborator.id})
    payload = {
        "role": "middle",
        "salary": 6000
    }
    response = api_client.patch(url, json.dumps(payload), content_type="application/json")

    assert response.status_code == HTTPStatus.OK
    assert collaborator.id == response.json()["id"]
    assert collaborator.role != response.json()["role"]

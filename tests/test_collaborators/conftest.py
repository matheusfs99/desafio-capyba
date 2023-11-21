import pytest


@pytest.fixture
def collaborator_payload():
    return {
        "name": "Test",
        "age": 20,
        "gender": "male",
        "role": "junior",
        "salary": 3000,
        "active": True,
    }
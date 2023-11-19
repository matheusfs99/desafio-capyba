import pytest


@pytest.fixture
def user_payload():
    return {
        "email": "test@example.com",
        "username": "testuser",
        "photo": None,
        "password": "testpassword"
    }

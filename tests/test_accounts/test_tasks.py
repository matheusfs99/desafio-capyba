import pytest
from django.core import mail
from apps.accounts.tasks import send_email, generate_token, validate_token

pytestmark = pytest.mark.django_db


def test_send_email():
    subject = "Test Subject"
    content = "Test Content"
    email = "testuser@example.com"

    send_email(email, subject, content)

    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == subject
    assert mail.outbox[0].body == content
    assert mail.outbox[0].to == [email]


def test_generate_token(user):
    user_id = user.id
    jwt_token = generate_token(user_id)

    assert jwt_token is not None


def test_validate_token(user):
    jwt_token = generate_token(user.id)

    validate_result = validate_token(jwt_token, user)

    assert validate_result

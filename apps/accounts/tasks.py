import hmac
import hashlib
import base64
import json
from datetime import datetime
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.response import Response


def send_email(email, subject, content):
    mail = EmailMessage(
        subject,
        content,
        "contato@email.com",
        [email],
        headers={
            "Replay-To": "contato@gmail.com"
        }
    )
    try:
        mail.send()
    except Exception as e:
        return Response({"error": e}, status=400)


def generate_token(user_id):
    header = json.dumps({
        "typ": "JWT",
        "alg": "HS256"
    }).encode()

    payload = json.dumps({
        "userId": user_id,
        "exp": None,
    }).encode()

    b64_header = base64.urlsafe_b64encode(header).decode()
    b64_payload = base64.urlsafe_b64encode(payload).decode()

    signature = hmac.new(
        key=settings.SECRET_KEY.encode(),
        msg=f"{b64_header}.{b64_payload}".encode(),
        digestmod=hashlib.sha256
    ).digest()

    jwt_token = f"{b64_header}.{b64_payload}.{base64.urlsafe_b64encode(signature).decode()}"

    return jwt_token


def validate_token(jwt, user):
    b64_header, b64_payload, b64_signature = jwt.split(".")
    b64_signature_checker = base64.urlsafe_b64encode(
        hmac.new(
            key=settings.SECRET_KEY.encode(),
            msg=f"{b64_header}.{b64_payload}".encode(),
            digestmod=hashlib.sha256
        ).digest()
    ).decode()

    payload = json.loads(base64.urlsafe_b64decode(b64_payload))
    unix_time_now = datetime.now().timestamp()

    if payload.get("exp") and payload["exp"] < unix_time_now:
        raise Exception("Token expirado")

    if b64_signature_checker != b64_signature:
        raise Exception("Assinatura inválida")

    validate = user.validate_user()

    return validate

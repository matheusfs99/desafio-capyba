import pytest
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.fixture
def terms_payload():
    return {
        "terms_of_use": SimpleUploadedFile("/media/terms_of_use.pdf", b"test"),
        "privacy_policies": SimpleUploadedFile("/media/privacy_policies.pdf", b"test")
    }

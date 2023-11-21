import re
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.terms.serializers import TermsSerializer

pytestmark = pytest.mark.django_db


def get_relative_path(path, filename):
    regex_pattern = r"/desafiocapyba(/media/{}\.pdf)".format(filename)
    match = re.search(regex_pattern, path)
    if match:
        print("MATCH: ", match.group(1))
        return match.group(1)


def test_user_serializer(terms):
    serializer = TermsSerializer(instance=terms)
    assert serializer.data == {
        "terms_of_use": get_relative_path(terms.terms_of_use.path, "term"),
        "privacy_policies": get_relative_path(terms.privacy_policies.path, "policies")
    }


def test_terms_serializer_without_required_fields():
    incomplete_data = {
        "terms_of_use": "test.pdf",
    }
    serializer = TermsSerializer(data=incomplete_data)
    assert not serializer.is_valid()


def test_terms_serializer_create(terms_payload):
    serializer = TermsSerializer(data=terms_payload)
    assert serializer.is_valid()
    validated_data = serializer.validated_data
    terms = serializer.create(validated_data)

    assert terms.id


def test_partial_update_terms_serializer(terms):
    old_term = terms.terms_of_use
    serializer = TermsSerializer(
        instance=terms,
        data={"terms_of_use": SimpleUploadedFile(
            "new_terms.pdf", b"test")},
        partial=True
    )
    serializer.is_valid(raise_exception=True)
    updated_terms = serializer.save()

    assert updated_terms.id == terms.id
    assert updated_terms.terms_of_use != old_term

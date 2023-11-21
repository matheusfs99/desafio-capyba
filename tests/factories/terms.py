import factory
from apps.terms.models import Terms


class TermsFactory(factory.Factory):
    terms_of_use = "term.pdf"
    privacy_policies = "policies.pdf"

    class Meta:
        model = Terms

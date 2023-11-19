import factory
from apps.terms.models import Terms


class TermsFactory(factory.Factory):
    class Meta:
        model = Terms

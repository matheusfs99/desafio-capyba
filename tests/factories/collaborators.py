import factory
from apps.collaborators.models import Collaborator


class CollaboratorFactory(factory.Factory):
    class Meta:
        model = Collaborator

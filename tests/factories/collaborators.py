import factory
from apps.collaborators.models import Collaborator


class CollaboratorFactory(factory.Factory):
    name = "Test"
    age = 20
    gender = "male"
    role = "junior"
    salary = 2000

    class Meta:
        model = Collaborator

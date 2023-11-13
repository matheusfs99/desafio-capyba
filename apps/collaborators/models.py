from django.db import models


class Collaborator(models.Model):
    class Gender(models.TextChoices):
        MALE = "male"
        FEMALE = "female"
        OTHER = "other"

    class Roles(models.TextChoices):
        INTERN = "intern"
        JUNIOR = "junior"
        MIDDLE = "middle"
        SENIOR = "senior"

    name = models.CharField("Nome", max_length=100)
    age = models.IntegerField("Idade")
    gender = models.CharField("Gênero", max_length=6, choices=Gender.choices)
    role = models.CharField("Cargo", max_length=6, choices=Roles.choices)
    salary = models.FloatField("Salário")
    active = models.BooleanField("Atuante", default=True)

    def __str__(self):
        return self.name

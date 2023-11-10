from django.db import models


class Terms(models.Model):
    terms_of_use = models.FileField("Termos de uso", upload_to="pdf_files/")
    privacy_policies = models.FileField("Políticas de privacidade", upload_to="pdf_files/")

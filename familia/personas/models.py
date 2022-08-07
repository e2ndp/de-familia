from django.db import models

class Personas(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateField(null=True, blank=True)
    cellphone = models.BigIntegerField(null=True, blank=True)
    
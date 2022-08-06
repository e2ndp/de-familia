from django.db import models

class Personas(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateField()
    cellphone = models.BigIntegerField()
    
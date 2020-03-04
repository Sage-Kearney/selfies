from django.db import models

# Create your models here.
class Selfie(models.Model):
    title = models.CharField(max_length=100)
    selfies_field = models.ImageField()
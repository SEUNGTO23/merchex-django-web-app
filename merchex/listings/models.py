from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
class Liste(models.Model):
    titre = models.fields.CharField(max_length=100)
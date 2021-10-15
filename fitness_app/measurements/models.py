from django.db import models

class Measurements(models.Model):
    user = models.IntegerField
    body_part = models.CharField(max_length=30)
    measurement = models.IntegerField()
    date = models.DateField()


from django.db import models

class Measurements(models.Model):
    user = models.IntegerField
    body_part = models.CharField(max_length=30)
    measurement = models.DecimalField(max_digits=6, decimal_places=1)
    date = models.DateField()


from django.db import models
from django.contrib.auth.models import User


class Measurements(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    body_part = models.CharField(max_length=30)
    measurement = models.IntegerField()
    date = models.DateField()


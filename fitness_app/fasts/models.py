from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, DateTimeField, TimeField

class Fasts(models.Model):
    user = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    total_duration = models.IntegerField()
    completed = models.BooleanField(default=False)
    
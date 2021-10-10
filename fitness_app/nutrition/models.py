from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

class MacroFolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=True)
    description = models.CharField(max_length=200, null=False, blank=True)
    


class Macros(models.Model):
    folder = models.ForeignKey(MacroFolder, on_delete=models.CASCADE)
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fats = models.IntegerField()

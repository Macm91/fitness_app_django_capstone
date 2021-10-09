from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields.files import ImageField


class WorkoutFolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_description = models.CharField(max_length=200, null=False, blank=True)
    folder_name = models.CharField(max_length=50, null=False, blank=False, default= "Workouts")


class Exercise (models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    body_part = models.CharField(max_length=50, null=False, blank=False)
    equipment = models.CharField(max_length=50, null=False, blank=False)
   

class Workout(models.Model):
    workout_folder = models.ForeignKey(WorkoutFolder, on_delete=models.CASCADE, null=False)
    notes = models.CharField(max_length=100, null=False, blank=True)

class WorkoutExercises(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False, default=1)
    workout =models.ForeignKey(Workout, on_delete=models.CASCADE, null=False, default=1)
    sets = models.IntegerField()
    reps = models.IntegerField()
    notes = models.CharField(max_length=100, null=False, blank=True) 
    
   

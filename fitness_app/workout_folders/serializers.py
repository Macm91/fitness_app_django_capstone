from django.db import models
from django.db.models import fields
from django.db.models.expressions import F
from rest_framework import serializers
from .models import Exercise, WorkoutHistory
from .models import WorkoutFolder
from .models import Workout
from .models import WorkoutExercises



class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'body_part', 'equipment']

# 
class WorkoutExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercises
        fields = ['id', 'exercise', 'workout', 'weight', 'sets', 'reps', 'notes']
#

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'workout_folder', 'notes', 'name']


class WorkoutFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutFolder
        fields = ['id', 'user', 'folder_description', 'folder_name']


          
class WorkoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutHistory
        fields = ['id', 'workout', 'date']

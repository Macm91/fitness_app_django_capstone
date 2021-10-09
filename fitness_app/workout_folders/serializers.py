from django.db.models import fields
from django.db.models.expressions import F
from rest_framework import serializers
from .models import Exercise
from .models import WorkoutFolder
from .models import Workout
from .models import WorkoutExercises



class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'body_part', 'equipment']


class WorkoutExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercises
        fields = ['id', 'exercise_id','sets', 'reps', 'notes']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'workout_folder_id', 'workout_exercise_id', 'notes']


class WorkoutFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutFolder
        fields = ['user_id', 'folder_description', 'folder_name']


        
from django.contrib import admin
from .models import WorkoutFolder
from .models import WorkoutExercises
from .models import Workout
from . models import Exercise
from .models import WorkoutHistory

# Register your models here.

admin.site.register(WorkoutFolder)
admin.site.register(WorkoutExercises)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(WorkoutHistory)
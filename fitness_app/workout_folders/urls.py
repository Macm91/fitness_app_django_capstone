from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views

# from fitness_app.WorkoutFolder.models import WorkoutExercises
from .views import ExerciseList
from .views import WorkoutExercisesList
from .views import WorkoutList
from . import views

urlpatterns = [

    # Exercises
    path('exercise/', views.ExerciseList.as_view()),

    # WorkoutExercises
    path('workoutexercises/', views.WorkoutExercisesList.as_view(), name='get'),
   
#    ####################################
    # Above = Confirmed endpoints. Below, not so much. 
    # ################################### 

 # WorkoutExercises
    # get details on just one workoutExercise
    path('workoutexercises/<int:pk>/', views.WorkoutExercisesList.as_view(), name = 'get_object'),
    # Edit a workoutexercise 
    path('workoutexercises/edit/<int:w_e_id>/', views.WorkoutExercisesList.as_view(), name='edit'),

# Workout 
    # Get all workouts
    path('workout/', views.WorkoutList.as_view(), name='get'),
  

# workout Folder
    # get all folders
    path('folders/', views.WorkoutFolderList.as_view()),


]
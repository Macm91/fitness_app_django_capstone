from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from . import views
from .views import add_exercise, edit_exercise, get_all_exrecises, user_folders, user_workouts, workout_exercises


urlpatterns = [

    path('exercises/', views.get_all_exrecises),
    path('exercises/<int:pk>/', views.edit_exercise),
    path('addexercise/', views.add_exercise),
    path('folders/', views.user_folders),
    path('workout/', views.user_workouts),
    path('workoutexercises/', views.workout_exercises),

]
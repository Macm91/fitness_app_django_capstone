from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from . import views
from .views import add_exercise, add_workouts, edit_exercise, edit_folder, get_all_exrecises, user_folders, user_workouts, workout_exercises


urlpatterns = [

    path('exercises/', views.get_all_exrecises),
    path('exercises/<int:pk>/', views.edit_exercise),
    path('addexercise/', views.add_exercise),
    path('folders/', views.user_folders),
    path('add/folder/', views.add_folders),
    path('folders/<int:pk>/', views.edit_folder),
    path('workout/folder/<int:fk>/', views.user_workouts),
    path('workout/edit/<int:pk>/', views.edit_workout),
    path('workout/add_workout/', views.add_workouts),
    path('workoutexercises/<int:fk>/', views.workout_exercises),
    path('workout/add/exercise/', views.add_workout_exercises),
    path('workout/edit/exercise/<int:pk>/', views.edit_workout_exercise),
    path('workout/history/', views.add_workout_history),
    path('workout/history/<int:fk>/', views.get_user_workout_history)

]
from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from . import views
# from .views import 


urlpatterns = [

    path('folder/', views.user_folders),

]
from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from . import views



urlpatterns = [

    path('', views.fasts),
   

]
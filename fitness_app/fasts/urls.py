from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from . import views



urlpatterns = [

    path('', views.fasts),
    path('<int:pk>/', views.edit_fast),
    path('all/<int:pk>', views.get_all_fasts),
   

]
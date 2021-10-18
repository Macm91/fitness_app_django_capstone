from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework import views
from measurements import views
from .views import add_measurement, get_all_measurements, edit_measurements


urlpatterns = [


    path('add/', views.add_measurement),
    path('all/', views.get_all_measurements),
    path('all/<int:fk>/', views.edit_measurements),
    

]
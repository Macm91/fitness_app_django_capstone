from django.db.models import fields
from django.db.models.expressions import F
from rest_framework import serializers
from .models import Measurements



class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = ['id', 'user', 'measurement', 'date']






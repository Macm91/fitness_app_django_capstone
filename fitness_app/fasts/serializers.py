from django.db.models import fields
from django.db.models.expressions import F
from rest_framework import serializers
from .models import Fasts


class FastsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fasts
        fields = ['id', 'user', 'start', 'end', 'totalduration', ' completed']


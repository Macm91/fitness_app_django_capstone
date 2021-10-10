from django.db.models import fields
from django.db.models.expressions import F
from rest_framework import serializers
from .models import MacroFolder
from .models import Macros

class MacroFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MacroFolder
        fields = ['id', 'name', 'description']


class MacrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macros
        fields = ['id', 'folder', 'protein', 'carbs', 'fats']



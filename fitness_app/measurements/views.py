from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls.base import reverse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Measurements
from .serializers import MeasurementsSerializer 
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_measurements(request):
    exercises = Measurements.objects.all()
    serializers = MeasurementsSerializer(exercises, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_measurement(request):
    serializers=MeasurementsSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
@permission_classes([AllowAny])
def edit_exercise(request, pk):

    if request.method == 'PUT':
        exercise = Measurements.objects.get(id = pk )
        serializer = MeasurementsSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        fast = Measurements.objects.get(id = pk )
        serializer = MeasurementsSerializer(fast, many=False)
        return Response(serializer.data)

    




#folder methods

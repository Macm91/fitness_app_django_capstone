from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls.base import reverse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Fasts
from .serializers import FastsSerializer 
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def fasts(request):
    serializer = FastsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
   
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_fasts(request, pk):
    fast = Fasts.objects.filter(user = pk )
    serializer = FastsSerializer(fast, many=True)
    return Response(serializer.data)

    
@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([AllowAny])
def edit_fast(request, pk):

    if request.method == 'POST':
        fast = Fasts.objects.get(id = pk )
        serializer = FastsSerializer(fast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        fast = Fasts.objects.get(id = pk )
        serializer = FastsSerializer(fast, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        fast = Fasts.objects.get(id = pk )
        fast.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)
    
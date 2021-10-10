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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def fasts(request):

    print(
        'User', f"{request.user.id}{request.user.email}{request.user.username}"
    )

    if request.method == 'POST':
        serializer = FastsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        folder = Fasts.objects.filter(user_id=request.user.id)
        serializer = FastsSerializer(folder, many=True)
        return Response(serializer.data)


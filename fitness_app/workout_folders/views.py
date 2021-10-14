from django.http.response import HttpResponse
from django.urls.base import reverse
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Workout
from .models import WorkoutExercises
from .models import WorkoutFolder
from .models import Exercise
from .serializers import WorkoutExercisesSerializer 
from .serializers import ExerciseSerializer
from .serializers import WorkoutSerializer
from .serializers import WorkoutFolderSerializer
from django.contrib.auth.models import User
from django.shortcuts import render 



# exercise methods

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_exrecises(request):
    exercises = Exercise.objects.all()
    serializers = ExerciseSerializer(exercises, many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def add_exercise(request):
    serializers=ExerciseSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
@permission_classes([AllowAny])
def edit_exercise(request, pk):

    if request.method == 'PUT':
        exercise = Exercise.objects.get(id = pk )
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        fast = Exercise.objects.get(id = pk )
        serializer = ExerciseSerializer(fast, many=False)
        return Response(serializer.data)

    




#folder methods


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_folders(request):
    print(
        'User', f"{request.user.id}{request.user.email}{request.user.username}"
    )
    # if request.method == 'POST':
    #     serializer = WorkoutFolderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'GET':
    folder = WorkoutFolder.objects.filter(user_id=request.user.id)
    serializer = WorkoutFolderSerializer(folder, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_folders(request):
    serializer = WorkoutFolderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([AllowAny])
def edit_folder(request, pk):

    if request.method == 'PUT':
        wf = WorkoutFolder.objects.get(id = pk )
        serializer = WorkoutFolderSerializer(wf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        wf = WorkoutFolder.objects.get(id = pk )
        serializer = WorkoutFolderSerializer(wf, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        wf = WorkoutFolder.objects.get(id = pk )
        wf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# workout methods

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def user_workouts(request):
#     if request.method == 'POST':
#         serializer = WorkoutSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         workout = Exercise.objects.all()
#         serializers = ExerciseSerializer(workout, many=True)
#         return Response(serializers.data)


#    path('workout/folder/<int:fk>/', views.user_workouts),

@api_view(['GET'])
@permission_classes([AllowAny])
def user_workouts(request, fk):
        workout = Workout.objects.filter(workout_folder_id = fk )
        serializers = WorkoutSerializer(workout, many=True)
        return Response(serializers.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def add_workouts(request):
    serializer = WorkoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([AllowAny])
def edit_workout(request, pk):

    if request.method == 'PUT':
        wf = Workout.objects.get(id = pk )
        serializer = WorkoutSerializer(wf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        wf = Workout.objects.get(id = pk )
        serializer = WorkoutSerializer(wf, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        wf = Workout.objects.get(id = pk )
        wf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#workoutexercises methods

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def workout_exercises(request):
#     if request.method == 'POST':
#         serializer = WorkoutExercisesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         w_e = WorkoutExercises.objects.all()
#         serializer = WorkoutExercisesSerializer(w_e, many=True)
#         return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AllowAny])
def workout_exercises(request, fk):
        w_e = WorkoutExercises.objects.filter(workout_id = fk)
        serializer = WorkoutExercisesSerializer(w_e, many=True)
        return Response(serializer.data)



@api_view(['POST'])
@permission_classes([AllowAny])
def add_workout_exercises(request):
    serializer = WorkoutExercisesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([AllowAny])
def edit_workout_exercise(request, pk):

    if request.method == 'PUT':
        wf = WorkoutExercises.objects.get(id = pk )
        serializer = WorkoutExercisesSerializer(wf, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        wf = WorkoutExercises.objects.get(id = pk )
        serializer = WorkoutExercisesSerializer(wf, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        wf = WorkoutExercises.objects.get(id = pk )
        wf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

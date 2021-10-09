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



class ExerciseList(APIView):

    permission_classes = [AllowAny]
    
    def get(self, request):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)


    def post (self, request):
        serializers=ExerciseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)



class WorkoutExercisesList(APIView):

    permission_classes =[AllowAny]

    def get(self, request):
        w_e = WorkoutExercises.objects.all()
        serializer = WorkoutExercisesSerializer(w_e, many=True)
        return Response(serializer.data)

    def post (self, request):
        serializers=WorkoutExercisesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


    # def details (self, pk):
    #     w_e = WorkoutExercises.objects.get(pk = pk)
    #     context = {
    #         'w_e' : w_e
    #     }
    #     return render( 'WorkoutExercises/details.html', context)



    def get_object(request ,pk):
        try:
            w_e = WorkoutExercises.objects.get(pk=pk)
            serializer = WorkoutExercisesSerializer(w_e, many=True)
            return Response(serializers.data)
        except WorkoutExercises.DoesNotExist:
            raise Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


    # def edit_w_e(self,request,pk):
    #         w_e = self.get_object(pk)
    #         serializer = WorkoutExercisesSerializer(w_e, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    # def edit(request, w_e_id):
    #     w_e= WorkoutExercises.objects.get(pk=w_e_id)
    #     if request.method== 'POST':
    #         w_e.exercise_id = request.POST.get('exercise_id')
    #         w_e.sets = request.POST.get('sets')
    #         w_e.reps = request.POST.get('reps')
    #         w_e.notes = request.POST.get('notes')
    #         w_e.save()
    #         return HttpResponse (reverse('WorkoutFolder: all_exercises_in_workout'))
    #     else:
    #         context ={
    #             'w_e' : w_e
    #         }
    #         return render (request, 'WorkoutFolder/edit.html', context)

    def delete(self, pk):
        w_e = self.get_object(pk)
        w_e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete(request, w_e_id):
    #     delete_workout_exercise = WorkoutExercises.objects.get(pk = w_e_id)
    #     if request.method == 'POST':
    #         WorkoutExercises.objects.filter(pk= w_e_id).delete()

    #         return HttpResponseRedirect(reverse('WorkoutExercises:get'))
    #     else:
    #         context = {
    #             'delete_workout_exercise': delete_workout_exercise
    #         }
    #         return render(request, 'workoutExercises/delete.html', context)


    

class WorkoutList(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request):
        workout = Workout.objects.all()
        serializer = WorkoutSerializer(workout, many=True)
        return Response(serializer.data)

    def post (self, request):
        serializers=WorkoutSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)
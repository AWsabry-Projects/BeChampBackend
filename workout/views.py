from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from Register_Login.models import Profile
from workout.models import workout_day,category,workout

from workout.serializers import workoutSerializer,categorySerializer,workoutDaySerializer,numberOfSets

# Create your views here.

def workout(request):
    return render(request, "workout.html",)


# APIs
    
class get_user_week_exercises(APIView):
    def get(self,request,email,week_number):
        all = workout_day.objects.filter(day__user__email = email, day__week_number = week_number,)
        deadline = Profile.objects.filter(email=email).get()
        serializer = workoutDaySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data, "subscription_deadline": deadline.subscription_deadline }, safe=False)


class get_user_daily_exercises(APIView):
    def get(self,request,email,day_number):
        all = workout_day.objects.filter(day__user__email = email, day__day_number = day_number,)
        deadline = Profile.objects.filter(email=email).get()
        serializer = workoutDaySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data, "subscription_deadline": deadline.subscription_deadline }, safe=False)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from Register_Login.models import Profile
from workout.models import day
from workout.serializers import workoutDaySerializer

# Create your views here.

def workout(request):
    return render(request, "workout.html",)


# APIs
    
class get_user_week_exercises(APIView):
    def get(self,request,email,):
        all = day.objects.filter(day__user__email = email,)
        deadline = Profile.objects.filter(email=email).get()
        serializer = workoutDaySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data, "subscription_deadline": deadline.subscription_deadline }, safe=False)


class get_user_daily_exercises(APIView):
    def get(self,request,email):
        all = day.objects.filter(day__user__email = email,)
        deadline = Profile.objects.filter(email=email).get()
        serializer = workoutDaySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data, "subscription_deadline": deadline.subscription_deadline }, safe=False)
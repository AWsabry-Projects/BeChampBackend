from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from Nutrition.models import Nutrition_day

from Nutrition.serializers import DaySerializer
# Create your views here.



def connection(request):
    return render(request, "connection.html",)

# APIs
class get_user_days(APIView):
    def get(self,request,email):
        all = Nutrition_day.objects.filter(user__email = email)
        serializer = DaySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)


from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from customization.models import Day

from customization.serializers import DaySerializer
# Create your views here.



def connection(request):
    return render(request, "connection.html",)

# APIs


    
class get_user_days(APIView):
    def get(self,request,email):
        all = Day.objects.filter(user__email = email)
        serializer = DaySerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)


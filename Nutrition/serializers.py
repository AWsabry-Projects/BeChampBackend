from rest_framework import serializers
from Nutrition.models import Meal,Nutrition_day
from Register_Login.serializers import UserSerializer



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    user = UserSerializer(allow_null = True)

    class Meta:
        model = Nutrition_day
        fields = '__all__'

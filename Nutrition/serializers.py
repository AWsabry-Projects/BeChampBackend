from rest_framework import serializers
from Nutrition.models import Component,Meal,Day
from Register_Login.serializers import UserSerializer

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    components = ComponentSerializer(many=True, allow_null = True)
    class Meta:
        model = Meal
        fields = '__all__'

class DaySerializer(serializers.ModelSerializer):
    user = UserSerializer(allow_null = True)
    meal_1 = MealSerializer(allow_null = True)
    meal_2 = MealSerializer(allow_null = True)
    meal_3 = MealSerializer(allow_null = True)
    meal_4 = MealSerializer(allow_null = True)
    meal_5 = MealSerializer(allow_null = True)
    meal_6 = MealSerializer(allow_null = True)
    meal_7 = MealSerializer(allow_null = True)

    class Meta:
        model = Day
        fields = '__all__'

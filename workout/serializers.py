from rest_framework import serializers
from workout.models import category,Exercise,day,Week, ClientPlan
from Register_Login.serializers import UserSerializer


class workoutPlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPlan
        fields = '__all__'


class numberOfSets(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = '__all__'


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class workoutSerializer(serializers.ModelSerializer):
    category_type = serializers.CharField(source='category_type.title',allow_null = True)
    class Meta:
        model = Exercise
        fields = '__all__'




class workoutDaySerializer(serializers.ModelSerializer):
    day = workoutPlanningSerializer(allow_null = True)
    workout = workoutSerializer(allow_null = True)
    category_type = serializers.CharField(source='day.category_type.title',allow_null = True)

    class Meta:
        model = day
        fields = '__all__'

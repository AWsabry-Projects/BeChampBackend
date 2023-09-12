from django.db import models
from BeChamp import settings
from Register_Login.models import Profile

# Create your models here.


meal_type = (
    ('PreBreakfast', 'PreBreakfast'),
    ('Breakfast', 'Breakfast'),
    ('PreWorkout ', 'PreWorkout'),
    ('After Workout', 'After Workout'),
    ('Dinner', 'Dinner'),
    ('After Dinner', 'After Dinner'),
)


class Component(models.Model):
    number_in_grams = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    number_of_calories = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        full_name = str(self.number_in_grams) + "g" + " " + self.name
        return str(full_name)
    
    class Meta:
        verbose_name_plural = "Components"


class Meal(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    meal_type = models.CharField(max_length=50, choices=meal_type, blank=True, null=True)    
    components = models.ManyToManyField(Component)
    created = models.DateTimeField(auto_now=True)
    finished = models.BooleanField(default=False)



    def __str__(self):
        return str(self.title)

    
    class Meta:
        verbose_name_plural = "Meals"


class Day(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='user')
    day_number = models.IntegerField(blank=True,null=True)
    meal_1 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_1')
    meal_2 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_2')
    meal_3 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_3')
    meal_4 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_4')
    meal_5 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_5',blank=True,null=True)
    meal_6 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_6',blank=True,null=True)
    meal_7 = models.ForeignKey(to= Meal, on_delete=models.CASCADE, related_name='meal_7',blank=True,null=True)
    created = models.DateTimeField(auto_now=True)
    Done = models.BooleanField(default=False)




    def __str__(self):
        return str(self.user.email)
    
    class Meta:
        verbose_name_plural = "Days"
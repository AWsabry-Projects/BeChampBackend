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


class Nutrition_day(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='user')
    day_number = models.PositiveIntegerField(blank=True,null=True)
    total_calories = models.PositiveIntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now=True)
    Done = models.BooleanField(default=False)




    def __str__(self):
        return str(self.user.full_name) + " " + "day" + str(self.day_number)
    
    class Meta:
        verbose_name_plural = "Nutrition Days"


class Meal(models.Model):
    components = models.TextField(max_length=300,blank=True,null=True)
    meal_type = models.CharField(max_length=50, choices=meal_type, blank=True, null=True)    
    created = models.DateTimeField(auto_now=True)
    finished = models.BooleanField(default=False)
    day = models.ForeignKey(to= Nutrition_day, on_delete=models.CASCADE, related_name='day')
    total_meal_calorie = models.PositiveIntegerField(blank=True,null=True)



    def __str__(self):
        return str(self.components)

    
    class Meta:
        verbose_name_plural = "Meals"

class pending_upgrades(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='clients')
    image = models.ImageField(blank=True,null=True)
    comment_from_client = models.TextField(max_length=300,blank=True,null=True)
    upgraded = models.BooleanField(default=True)



    def __str__(self):
        return str(self.user.full_name)
    

    def save(self, *args, **kwargs):
        if self.upgraded == True:
            Nutrition_day.objects.update_or_create(user= self.user,day_number=1)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=2)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=3)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=4)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=5)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=6)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=7)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=8)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=9)
            Nutrition_day.objects.update_or_create(user= self.user,day_number=10)
            super().save(*args, **kwargs)
        else:
            print("bas ya 7omar")
            super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Pending Upgrades"
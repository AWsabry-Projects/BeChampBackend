from django.db import models

from Register_Login.models import Profile

# Create your models here.

class category(models.Model):
    title = models.CharField(blank=True,null= True, max_length= 100)
    arabic_title = models.CharField(blank=True,null= True, max_length= 100)
    category = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True,null= True, max_length= 500)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name_plural = "Categories"


class workout(models.Model):
    title = models.CharField(blank=True,null= True, max_length= 100)
    arabic_title = models.CharField(blank=True,null= True, max_length= 100)
    category = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "Workouts"

class client_workout(models.Model):
    day_number = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(category)
    workouts = models.ManyToManyField(workout)
    finished = models.BooleanField(default=False)
    week_number = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return {"Day" + " " + str(self.day_number)}
    class Meta:
        verbose_name_plural = "Workout Days"


class workout_day(models.Model):
    day_number = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(category)
    workouts = models.ManyToManyField(workout)
    finished = models.BooleanField(default=False)
    week_number = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return {"Day" + " " + str(self.day_number)}
    class Meta:
        verbose_name_plural = "Workout Days"

class workout_week(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='client')
    created = models.DateTimeField(auto_now=True)
    finished = models.BooleanField(default=False)
    week_number = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.user)
    class Meta:
        verbose_name_plural = "Weeks"

from django.db import models
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
from Register_Login.models import Profile
from django.contrib import messages
from django.http import HttpResponse

# Create your models here.

choices = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
)

week_choices = (
    ('Week 1','Week 1'),
    ('Week 2','Week 2'),
    ('Week 3','Week 3'),
    ('Week 4','Week 4'),

)

class category(models.Model):
    title = models.CharField(blank=True,null= True, max_length= 100)
    arabic_title = models.CharField(blank=True,null= True, max_length= 100)
    created = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True,null= True, max_length= 500)

    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "Categories"


def validate_gif_extension(value):
    if not value.name.lower().endswith('.gif'):
        raise ValidationError('Only GIF files are allowed.')
    

class Exercise(models.Model):
    title = models.CharField(blank=True,null= True, max_length= 100)
    arabic_title = models.CharField(blank=True,null= True, max_length= 100)
    gif_file = models.FileField(upload_to='uploads/workouts', validators=[FileExtensionValidator(allowed_extensions=['gif'])])
    category_type = models.ForeignKey(to= category, on_delete=models.CASCADE, related_name= 'type')
    description = models.TextField(blank=True,null= True, max_length= 500)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name_plural = "Workouts"


class ClientPlan(models.Model):
    user = models.OneToOneField(to= Profile, on_delete=models.CASCADE,unique=True, related_name='cl')
    repeat_week_one = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user) 
    class Meta:
        verbose_name_plural = "Client's Plans"
        verbose_name = "Client's Plan"

class Week(models.Model):
    week_number = models.CharField(
        max_length=50, choices=week_choices,)    
    client_plan = models.ForeignKey(to= ClientPlan, on_delete=models.CASCADE, related_name='plans')
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.week_number)
    
    class Meta:
        verbose_name_plural = "Weeks"
    


class day(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='userss')
    category = models.ForeignKey(to= category, on_delete=models.CASCADE, related_name='cat')
    created = models.DateTimeField(auto_now=True)
    week = models.ForeignKey(to= Week, on_delete=models.CASCADE, related_name='weeks')
    day_number = models.PositiveIntegerField()
    done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.user = self.week.client_plan.user
        check_exist = day.objects.filter(user=self.user, week__week_number=self.week).exists()
        print(self.user)
        print(self.week)
        print(check_exist)
        if check_exist:
            response = HttpResponse("The user has the same week planned before.", content_type="text/plain")
            return response
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user) + " " + "Day" + " " + str(self.day_number)
    class Meta:
        verbose_name_plural = "Client Exercise's Days"
        verbose_name = "Day"


        
class user_exercise(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='userssss')
    day = models.ForeignKey(to= day, on_delete=models.CASCADE, related_name='days')
    exercise = models.ForeignKey(to= Exercise, on_delete=models.CASCADE, related_name='workouts')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.exercise.title)
    class Meta:
        verbose_name_plural = "User Exercises"
        verbose_name = "Exercise"



class workout_reps(models.Model):
    user_workout = models.ForeignKey(to= user_exercise, on_delete=models.CASCADE, related_name='workouts')
    sets = models.PositiveIntegerField()
    reps = models.PositiveBigIntegerField()
    rest_time = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.sets)
    class Meta:
        verbose_name_plural = "Exercise's reps"
        verbose_name = "Exercise rep"
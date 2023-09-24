from django.db import models
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
from Register_Login.models import Profile

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
    ('week_1','week_1'),
    ('week_2','week_2'),
    ('week_3','week_3'),
    ('week_4','week_4'),

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
    

class workout(models.Model):
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







class workoutPlanning(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='cl')
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user) 
    class Meta:
        verbose_name_plural = "Workout Plans"

class Week(models.Model):
    workoutplan = models.ForeignKey(to= workoutPlanning, on_delete=models.CASCADE, related_name='plans')
    
    def __str__(self):
        return f"Days"
    
    class Meta:
        verbose_name_plural = "Weeks"
    


class day(models.Model):
    created = models.DateTimeField(auto_now=True)
    week = models.ForeignKey(to= Week, on_delete=models.CASCADE, related_name='weeks')

    def __str__(self):
        return str(self.workout.title)
    class Meta:
        verbose_name_plural = "Workout Days"
    
class user_workout(models.Model):
    day = models.ForeignKey(to= day, on_delete=models.CASCADE, related_name='days')
    workout = models.ForeignKey(to= workout, on_delete=models.CASCADE, related_name='workouts')
    sets = models.PositiveIntegerField()
    reps = models.PositiveBigIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.workout.title)
    class Meta:
        verbose_name_plural = "Workout Days"



class TopLevel(models.Model):
    name = models.CharField(max_length=200)

class LevelOne(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey(to= TopLevel,on_delete=models.CASCADE)

class LevelTwo(models.Model):
    name = models.CharField(max_length=200)
    level = models.ForeignKey(to= LevelOne,on_delete=models.CASCADE)
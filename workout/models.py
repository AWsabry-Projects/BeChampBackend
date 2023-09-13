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
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='userClient')
    week_number = models.CharField(choices=week_choices, blank=True,null=True,max_length=50)
    day_number = models.CharField(choices=choices, blank=True,null=True,max_length=50)
    category_type = models.ForeignKey(to= category, on_delete=models.CASCADE, related_name= 'catType')
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user) + " " + "Day" + " " + str(self.day_number)+ " " + str(self.week_number) + " " + str(self.category_type.title) 
    class Meta:
        verbose_name_plural = "workoutPlanning"


class workout_day(models.Model):
    day = models.ForeignKey(to= workoutPlanning, on_delete=models.CASCADE, related_name= 'daily')
    created = models.DateTimeField(auto_now=True)
    workout = models.ForeignKey(to= workout, on_delete=models.CASCADE, related_name= 'work')
    finished = models.BooleanField(default=False)

    def __str__(self):
        return str(self.workout.title)
    class Meta:
        verbose_name_plural = "Workout Days"


class number_of_sets(models.Model):
    workout_day = models.ForeignKey(to=workout_day, on_delete=models.CASCADE, related_name='sets')
    number_of_sets = models.PositiveIntegerField()
    number_of_reps = models.PositiveIntegerField()

    def __str__(self):
        return f"Sets: {self.number_of_sets}, Reps: {self.number_of_reps}"
    


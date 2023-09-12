from django.db import models
from django.core.validators import FileExtensionValidator
from django.forms import ValidationError
from Register_Login.models import Profile

# Create your models here.

choices = (
    ('Day 1','Day 1'),
    ('Day 2','Day 2'),
    ('Day 3','Day 3'),
    ('Day 4','Day 4'),
    ('Day 5','Day 5'),
    ('Day 6','Day 6'),
    ('Day 7','Day 7'),

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



class workout_week(models.Model):
    user = models.ForeignKey(to= Profile, on_delete=models.CASCADE, related_name='client')
    created = models.DateTimeField(auto_now=True)
    finished = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)
    week_number = models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.user) + "   " + "week" + str(self.week_number)
    class Meta:
        verbose_name_plural = "Weeks"


class workout_day(models.Model):
    day_number = models.CharField(choices=choices, blank=True,null=True,max_length=50)
    created = models.DateTimeField(auto_now=True)
    workout = models.ForeignKey(to= workout, on_delete=models.CASCADE, related_name= 'work')
    category_type = models.ForeignKey(to= category, on_delete=models.CASCADE, related_name= 'cat')
    finished = models.BooleanField(default=False)
    week = models.ForeignKey(to= workout_week, on_delete=models.CASCADE, related_name='week')

    def __str__(self):
        return str(self.day_number)
    class Meta:
        verbose_name_plural = "Workout Days"


class number_of_sets(models.Model):
    workout_day = models.ForeignKey(to=workout_day, on_delete=models.CASCADE, related_name='sets')
    number_of_sets = models.PositiveIntegerField()
    number_of_reps = models.PositiveIntegerField()

    def __str__(self):
        return f"Sets: {self.number_of_sets}, Reps: {self.number_of_reps}"
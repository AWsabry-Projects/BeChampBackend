from django.contrib import admin

from Register_Login.models import Profile
from .models import Week, user_workout, workout,category, workout_reps, workoutPlanning,day
from django.db import models
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
import nested_admin
# Register your models here.

class workout_Admin(admin.ModelAdmin):    
    list_filter = ("category_type",)
    list_display = ("title","arabic_title","created")
    raw_id_fields = ('category_type',)
    autocomplete_fields = ['category_type']
    search_fields = ['title','arabic_title','category_type']



class categoryAdmin(admin.ModelAdmin):    
    list_filter = ("title",)
    list_display = ("title","arabic_title","created")
    search_fields = ['title','arabic_title']

class user_workout_reps_Admin(nested_admin.NestedStackedInline):    
    model = workout_reps
    extra = 1  # Number of empty forms to display
    max_num = 10



class user_workout_Admin(nested_admin.NestedStackedInline):    
    model = user_workout
    extra = 1  # Number of empty forms to display 
    inlines = [user_workout_reps_Admin]


class day_Admin(nested_admin.NestedStackedInline): 
    model = day
    extra = 0  # Number of empty forms to display
    max_num = 7
    inlines = [user_workout_Admin]
    exclude = ['done']
    
 

class week_inline(nested_admin.NestedStackedInline):  # or admin.StackedInline for a different display
    model = Week
    extra = 4  # Number of empty forms to display
    max_num = 4
    inlines = [day_Admin]
    exclude = ['done']


    

class workoutPlans(nested_admin.NestedModelAdmin):    
    list_filter = ("user__full_name",)
    search_fields = ['user__full_name',]
    inlines = [week_inline,]





admin.site.register(workout,workout_Admin,)
# admin.site.register(day,day_Admin)
admin.site.register(category,categoryAdmin)
admin.site.register(workoutPlanning,workoutPlans)



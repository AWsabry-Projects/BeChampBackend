from django.contrib import admin

from Register_Login.models import Profile
from .models import number_of_sets, workout,workout_day,category, workoutPlanning
from django.db import models


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



class SetInline(admin.TabularInline):  # or admin.StackedInline for a different display
    model = number_of_sets
    extra = 1  # Number of empty forms to display


class workout_day_Admin(admin.ModelAdmin):    
    list_filter = ("workout",)
    list_display = ("training", "day","finished","created")
    raw_id_fields = ('workout','day',)
    # autocomplete_fields = ['workout','day']
    search_fields = ['day__user__full_name', 'day__user__email', 'day__user__phone_number', 'day__some_other_field']
    inlines = [SetInline]

    def training(self, obj):
        return str(obj.workout)
    
    






admin.site.register(workout,workout_Admin)
admin.site.register(workout_day,workout_day_Admin)
admin.site.register(category,categoryAdmin)
admin.site.register(workoutPlanning,)

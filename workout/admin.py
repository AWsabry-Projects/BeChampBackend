from django.contrib import admin

from Register_Login.models import Profile
from .models import number_of_sets, workout,workout_day,workout_week,category
from django.db import models


# Register your models here.

class workout_Admin(admin.ModelAdmin):    
    list_filter = ("category_type",)
    list_display = ("title","arabic_title","created")
    raw_id_fields = ('category_type',)
    autocomplete_fields = ['category_type']
    search_fields = ['title','arabic_title','category_type']

class workout_week_Admin(admin.ModelAdmin):    
    list_filter = ("user",)
    list_display = ("weekName","finished","expired","created")
    raw_id_fields = ('user',)
    autocomplete_fields = ['user']
    search_fields = ['user__email','user__full_name']

    def weekName(self, obj):
        return str(obj.user.full_name) + "   " + "week" + str(obj.week_number)






class categoryAdmin(admin.ModelAdmin):    
    list_filter = ("title",)
    list_display = ("title","arabic_title","created")
    search_fields = ['title','arabic_title']



class SetInline(admin.TabularInline):  # or admin.StackedInline for a different display
    model = number_of_sets
    extra = 1  # Number of empty forms to display


class workout_day_Admin(admin.ModelAdmin):    
    list_filter = ("workout","week__user__full_name","category_type")
    list_display = ("training", "name_and_week", "day_number","category_type","finished","created")
    raw_id_fields = ('workout','week','category_type')
    autocomplete_fields = ['workout','week','category_type']
    search_fields = ['week__user__full_name','week__user__email','week__user__phone_number']
    inlines = [SetInline]

    def training(self, obj):
        return str(obj.workout)
    
    def name_and_week(self, obj):
        return str(obj.week)





admin.site.register(workout,workout_Admin)
admin.site.register(workout_day,workout_day_Admin)
admin.site.register(workout_week,workout_week_Admin)
admin.site.register(category,categoryAdmin)

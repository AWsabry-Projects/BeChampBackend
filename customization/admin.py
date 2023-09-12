from django.contrib import admin
from .models import Day,Component,Meal
from django.db import models
from django.forms import CheckboxSelectMultiple
# Register your models here.


class ClientDays(admin.ModelAdmin):
    list_filter = ("user",)
    list_display = ("user","day_number","created","meal_1","meal_2","meal_3","meal_4","meal_5","meal_6","meal_7")


class ComponentsAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    # list_display = ("name",)

class MealAdmin(admin.ModelAdmin):
    list_filter = ("title","meal_type")
    list_display = ("title","meal_type","created")

    formfield_overrides = {
        models.ManyToManyField : {'widget' : CheckboxSelectMultiple},
    }


admin.site.register(Day, ClientDays)
admin.site.register(Component, ComponentsAdmin)
admin.site.register(Meal, MealAdmin)
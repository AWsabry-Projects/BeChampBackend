from django.contrib import admin
from .models import Nutrition_day,Meal,pending_upgrades
from django.db import models
from django.forms import CheckboxSelectMultiple
import nested_admin

# Register your models here.





class meal_Admin(admin.TabularInline): 
    model = Meal
    extra = 1  # Number of empty forms to display
    exclude = ['done','finished']
    

    formfield_overrides = {
        models.ManyToManyField : {'widget' : CheckboxSelectMultiple},
    }


class DaysAdmin(admin.ModelAdmin):
    list_filter = ("user",)
    list_display = ("user_name","created",)
    inlines = [meal_Admin]
    exclude = ['done']

    def user_name(self, obj):
        return  str(obj.user.full_name) + " " + "day" + str(obj.day_number)

admin.site.register(Nutrition_day, DaysAdmin)
admin.site.register(pending_upgrades,)
# admin.site.register(Meal, MealAdmin)
from django.contrib import admin

from Register_Login.models import Profile
from .models import Week, user_workout, workout,category, workoutPlanning,day,TopLevel,LevelOne,LevelTwo
from django.db import models
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

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


class user_workout_Admin(NestedStackedInline):    
    model = user_workout
    extra = 1  # Number of empty forms to display 


class day_Admin(NestedStackedInline):    
    model = day
    extra = 1  # Number of empty forms to display
    max_num = 7
    inlines = [user_workout_Admin]
 

class week_inline(NestedStackedInline):  # or admin.StackedInline for a different display
    model = Week
    extra = 1  # Number of empty forms to display
    max_num = 4
    inlines = [day_Admin]


    

class workoutPlans(NestedModelAdmin):    
    list_filter = ("user__full_name",)
    search_fields = ['user__full_name',]
    inlines = [week_inline,]




class LevelTwoInline(NestedStackedInline):
    model = LevelTwo
    extra = 1
    fk_name = 'level'



class LevelOneInline(NestedStackedInline):
    model = LevelOne
    extra = 1
    fk_name = 'level'
    inlines = [LevelTwoInline]


class TopLevelAdmin(NestedModelAdmin):
    model = TopLevel
    inlines = [LevelOneInline]


admin.site.register(TopLevel, TopLevelAdmin)
admin.site.register(workout,workout_Admin,)
# admin.site.register(day,day_Admin)
admin.site.register(category,categoryAdmin)
admin.site.register(workoutPlanning,workoutPlans)



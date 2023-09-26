from django.contrib import admin
from .models import Week, Exercise, user_exercise,category, workout_reps, ClientPlan,day
import nested_admin
# Register your models here.

class exercises_Admin(admin.ModelAdmin):    
    list_filter = ("category_type","created")
    list_display = ("title","arabic_title","category_type","created")
    raw_id_fields = ('category_type',)
    autocomplete_fields = ['category_type']
    search_fields = ['title','arabic_title','category_type']



class categoryAdmin(admin.ModelAdmin):    
    list_filter = ("title",)
    list_display = ("title","arabic_title","created")
    search_fields = ['title','arabic_title']



class day_inline_Admin(nested_admin.NestedStackedInline): 
    model = day
    extra = 0  # Number of empty forms to display
    max_num = 7
    exclude = ['user','done']
    
 

class week_inline(nested_admin.NestedStackedInline):  # or admin.StackedInline for a different display
    model = Week
    extra = 0 # Number of empty forms to display
    max_num = 4
    inlines = [day_inline_Admin]
    exclude = ['done']



class workoutPlans(nested_admin.NestedModelAdmin):    
    list_filter = ("user__full_name","repeat_week_one","created")
    list_display = ("user","repeat_week_one","goal","created","end_of_subscription","subscription_type","gender","phone_number")
    search_fields = ['user__full_name','user__email']
    inlines = [week_inline,]

    def end_of_subscription(self, obj):
        return str(obj.user.subscription_deadline)
    def subscription_type(self, obj):
        return str(obj.user.subscription_type)
    def gender(self, obj):
        return str(obj.user.gender)
    def goal(self, obj):
        return str(obj.user.goal)
    def phone_number(self, obj):
        return str(obj.user.phone_number)

class workout_reps_admin(nested_admin.NestedStackedInline):    
    model = workout_reps
    extra = 1  # Number of empty forms to display


class user_exercise_admin(nested_admin.NestedStackedInline):
    model = user_exercise
    exclude = ['user']
    extra = 1  # Number of empty forms to display
    inlines = [workout_reps_admin,]


class day_admin(nested_admin.NestedModelAdmin):    
    list_filter = ('week__client_plan__user__full_name','week__week_number','category',"created")
    list_display = ("display_name","week","category","created","done")
    search_fields = ['user__full_name','user__email']
    readonly_fields = ['user','category','week','day_number','done']
    inlines = [user_exercise_admin,]


    def display_name(self, obj):
        return  str(obj.user.full_name) + " " + "Day" + str(obj.day_number)


admin.site.register(Exercise,exercises_Admin,)
admin.site.register(category,categoryAdmin) # Filters added fully
admin.site.register(ClientPlan,workoutPlans) # Filters added fully
admin.site.register(day,day_admin) # Filters added fully


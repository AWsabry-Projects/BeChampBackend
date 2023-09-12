from Register_Login.models import Profile
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_filter = ("email","full_name", "phone_number", "last_modified")
    list_display = ("email","full_name", 'phone_number','last_modified','goal','is_active','last_modified'
                  )
    search_fields = ['email','full_name',]




admin.site.register(Profile, UserAdmin)




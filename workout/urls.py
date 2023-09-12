from django.urls import path,re_path
from workout import views

app_name = 'workout'

urlpatterns = [
    path('workout/',view = views.workout, name = "workout"),
]

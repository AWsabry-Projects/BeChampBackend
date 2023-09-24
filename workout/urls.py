from django.urls import path,re_path
from workout import views

app_name = 'workout'

urlpatterns = [
    path('workout/',view = views.workout, name = "workout"),
    # path('get_user_week_exercises/<str:email>/<str:week_number>', view=views.get_user_week_exercises.as_view(), name='get_user_week_exercises'),
    # path('get_user_daily_exercises/<str:email>/<str:day_number>', view=views.get_user_daily_exercises.as_view(), name='get_user_daily_exercises'),

]

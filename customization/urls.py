from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from customization import views

app_name = 'customization'

urlpatterns = [
    path('connection',view = views.connection, name = "connection"),
    path('get_user_days/<str:email>', view=views.get_user_days.as_view(), name='get_user_days'),

]

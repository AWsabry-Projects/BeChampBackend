# Generated by Django 4.1.2 on 2023-09-13 00:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("workout", "0017_alter_workout_day_day"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="workoutDayTitle",
            new_name="workoutPlanning",
        ),
        migrations.DeleteModel(
            name="workout_week",
        ),
    ]

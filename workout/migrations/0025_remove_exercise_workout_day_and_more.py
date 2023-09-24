# Generated by Django 4.1.2 on 2023-09-23 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0024_client_workoutplan_workoutweek_workoutday_exercise"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="exercise",
            name="workout_day",
        ),
        migrations.RemoveField(
            model_name="workoutday",
            name="workout_week",
        ),
        migrations.RemoveField(
            model_name="workoutplan",
            name="client",
        ),
        migrations.RemoveField(
            model_name="workoutweek",
            name="workout_plan",
        ),
        migrations.DeleteModel(
            name="Client",
        ),
        migrations.DeleteModel(
            name="Exercise",
        ),
        migrations.DeleteModel(
            name="WorkoutDay",
        ),
        migrations.DeleteModel(
            name="WorkoutPlan",
        ),
        migrations.DeleteModel(
            name="WorkoutWeek",
        ),
    ]

# Generated by Django 4.1.2 on 2023-09-24 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0031_remove_workoutplanning_category_type_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workoutplanning",
            name="day",
        ),
    ]

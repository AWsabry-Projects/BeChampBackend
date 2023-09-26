# Generated by Django 4.1.2 on 2023-09-26 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workout", "0058_rename_workoutplan_week_client_plan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="week",
            name="week_number",
            field=models.CharField(
                blank=True,
                choices=[
                    ("week_1", "week_1"),
                    ("week_2", "week_2"),
                    ("week_3", "week_3"),
                    ("week_4", "week_4"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]

# Generated by Django 4.1.2 on 2023-09-12 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("customization", "0004_component"),
    ]

    operations = [
        migrations.CreateModel(
            name="Meal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "meal_number",
                    models.IntegerField(blank=True, max_length=10, null=True),
                ),
                ("created", models.DateTimeField(auto_now=True)),
                (
                    "component_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="component_1",
                        to="customization.component",
                    ),
                ),
                (
                    "component_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="component_2",
                        to="customization.component",
                    ),
                ),
                (
                    "component_3",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="component_3",
                        to="customization.component",
                    ),
                ),
                (
                    "component_4",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="component_4",
                        to="customization.component",
                    ),
                ),
                (
                    "component_5",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="component_5",
                        to="customization.component",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Meals",
            },
        ),
    ]

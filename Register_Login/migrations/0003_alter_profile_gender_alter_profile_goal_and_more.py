# Generated by Django 4.1.2 on 2023-09-12 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Register_Login", "0002_alter_profile_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="goal",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="height",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="subscription_deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="weight",
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-18 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrer", "0006_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
# Generated by Django 5.2 on 2025-04-04 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_flight_icon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.2 on 2025-04-16 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_city_image_city_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='images',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]

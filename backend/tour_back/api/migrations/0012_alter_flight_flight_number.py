# Generated by Django 5.2 on 2025-04-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_tour_end_date_remove_tour_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=10),
        ),
    ]

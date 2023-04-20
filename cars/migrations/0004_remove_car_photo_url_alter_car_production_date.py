# Generated by Django 4.1.7 on 2023-04-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_url_alter_car_production_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='photo_url',
        ),
        migrations.AlterField(
            model_name='car',
            name='production_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
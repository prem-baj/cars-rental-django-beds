# Generated by Django 4.1.7 on 2023-03-27 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0002_car_carmodel_rename_brand_carbrand_delete_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_date', models.DateTimeField()),
                ('drop_off_date', models.DateTimeField()),
                ('payment_method', models.CharField(choices=[('1', 'Card'), ('2', 'Cash')], max_length=1)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
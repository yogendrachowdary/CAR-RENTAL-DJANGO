# Generated by Django 4.2.5 on 2023-10-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resadmin', '0010_car_manufacturer_car_price_car_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]

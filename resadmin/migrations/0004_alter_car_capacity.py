# Generated by Django 4.2.5 on 2023-09-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resadmin', '0003_alter_car_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='capacity',
            field=models.IntegerField(choices=[(8, 8), (4, 4)]),
        ),
    ]

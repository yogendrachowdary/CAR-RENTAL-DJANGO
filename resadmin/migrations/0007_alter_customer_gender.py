# Generated by Django 4.2.5 on 2023-09-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resadmin', '0006_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], max_length=10),
        ),
    ]

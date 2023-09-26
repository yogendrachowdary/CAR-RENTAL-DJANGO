from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table="admin_table"


class Customer(models.Model):
    id=models.AutoField(primary_key=True)
    customerid=models.BigIntegerField(blank=False,unique=True)
    city=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    age=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=150,blank=False,default="12345")
    email=models.CharField(max_length=120,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="customer_table"

class Car(models.Model):
    id=models.AutoField(primary_key=True)
    model=models.CharField(max_length=100)
    color=models.CharField(max_length=150)
    capacity=models.IntegerField(blank=False)

    class Meta:
        db_table="car_table"





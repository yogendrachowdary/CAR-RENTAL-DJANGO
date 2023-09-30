from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table="admin_table"

    def __str__(self):
        return self.username

        


class Customer(models.Model):
    customerid=models.AutoField(primary_key=True)
    city=models.CharField(max_length=100,blank=False)
    name=models.CharField(max_length=100,blank=False)
    gender_choices=(("male","MALE"),("female","FEMALE"))
    gender=models.CharField(max_length=10,blank=False,choices=gender_choices)
    age=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=150,blank=False,default="12345")
    email=models.CharField(max_length=120,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="customer_table"
    
    def __str__(self):
        return self.name
    
    # if you want to make this to customerid you should do this and convert into string
    # def __str__(self):
    #     return str(self.customerid)
    

class Car(models.Model):
    id=models.AutoField(primary_key=True)
    model=models.CharField(max_length=100)
    color_choices=(("red","RED"),("black","BLACK"),("white","WHITE"),("blue","BLUE"))
    color=models.CharField(max_length=150,choices=color_choices)
    capacity_choice=((8,8),(4,4))
    capacity=models.IntegerField(blank=False,choices=capacity_choice)

    class Meta:
        db_table="car_table"
    
    def __str__(self):
        return self.model



class Owner(models.Model):
    ownerid = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    gender_choices = (("male", "MALE"), ("female", "FEMALE"))
    gender = models.CharField(max_length=10, blank=False, choices=gender_choices)
    age = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=150, blank=False, default="12345")
    email = models.CharField(max_length=120, blank=False, unique=True)
    contact = models.CharField(max_length=20, blank=False, unique=True)

    class Meta:
        db_table = "owner_table"
    
    def __str__(self):
        return self.name



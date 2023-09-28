from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q



from resadmin.models import Admin, Car, Customer


# Create your views here.

def adminhome(request):
    return render(request, "adminhome.html")

def changepassword(request):
    return render(request, "changepassword.html")

def viewcustomers(request):
    customer=Customer.objects.all()
    count=Customer.objects.count()
    return render(request, "viewcustomers.html",{"customerdata":customer,"count":count})

def viewcars(request):
    car=Car.objects.all()
    count=Car.objects.count()
    return render(request, "viewcars.html",{"cardata":car,"count":count})

def admincars(request):
    return render(request,"admincars.html")

from django.shortcuts import render, redirect
from .models import Car  # Import the Car model

def addcar(request):
    if request.method == "POST":
        model = request.POST["model"]
        color = request.POST["color"]
        capacity = request.POST["capacity"]

        car = Car(
            model=model,
            color=color,
            capacity=capacity
        )
        Car.save(car)

        msg = "Car added Successfully!!"

        return render(request, "addcar.html", {"msg": msg})

    return render(request, "addcar.html")


def updatecar(request):
    return render(request,"updatecar.html")

def deletecar(request):
    return render(request,"deletecar.html")

def admincustomers(request):
    return render(request,"admincustomers.html")

def addcustomer(request):
    if request.method == "POST":
        city = request.POST["city"]
        name = request.POST["name"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        password = request.POST["password"]
        email = request.POST["email"]
        contact = request.POST["contact"]

        customer = Customer(
            city=city,
            name=name,
            gender=gender,
            age=age,
            password=password,
            email=email,
            contact=contact
        )
        Customer.save(customer)

        msg="Customer added Successfully!!"

        return render(request,"addcustomer.html",{"msg":msg})

    return render(request, "addcustomer.html")



    return render(request,"addcustomer.html")

def updatecustomer(request):
    return render(request,"updatecustomer.html")

def deletecustomer(request):
    return render(request,"deletecustomer.html")


def adminlogout(request):
    return render(request, "login.html")

def checkadminlogin(request):
    if request.method=="POST":
        adminuname=request.POST["uname"]  #request.GET["uname"]
        adminpwd=request.POST["pwd"]      #request.GET["pwd"]

        flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))  #it will check in Admin table objects(rows) for username and password. Q means query
        if flag:
            return render(request,"adminhome.html")
        else:
            return HttpResponse("Login Failed")



    
    





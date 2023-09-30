from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from .forms import AddOwnerForm



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
    customer=Customer.objects.all()
    count=Customer.objects.count()
    return render(request, "updatecustomer.html",{"customerdata":customer,"count":count})

def customerupdation(request,cid):
    if request.method == "POST":
            customer = Customer.objects.get(pk=cid)
            # Update customer fields with new data
            customer.city = request.POST["city"]
            customer.name = request.POST["name"]
            customer.gender = request.POST["gender"]
            customer.age = request.POST["age"]
            customer.password = request.POST["password"]
            customer.email = request.POST["email"]
            customer.contact = request.POST["contact"]
            Customer.save(customer)
            return redirect("viewcustomers")
    cus=Customer.objects.get(pk=cid)   #here pk means primary key it is keyword in django            
    # return render(request,"customerupdation",{"cus":cus})
    return render(request,"newcustomervalue.html",{"cus":cus})


def deletecustomer(request):
    customer=Customer.objects.all()
    count=Customer.objects.count()
    return render(request, "deletecustomer.html",{"customerdata":customer,"count":count})

def customerdeletion(request,cid):
    #Customer.objects.filter(customerid=cid).delete()   #here we are filtering based on id
    # return HttpResponse("customerdeleted successfullly")
    #WE can also write like this
    cus=Customer.objects.get(pk=cid)   #here pk means primary key it is keyword in django
    cus.delete()
    return redirect("viewcustomers")
    


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


def adminowners(request):
    return render(request,"adminowners.html")
    
def addowner(request):
    form=AddOwnerForm()   #non parameterized constructor
    if request.method=="POST":
        form1=AddOwnerForm(request.POST)   #here request.POST means form data-parameterized constructor
        if form1.is_valid:
            form1.save()   #this will save the form data in the owner_table
            # return HttpResponse("added successfully")
            msg="Owner added Successfully"
            return render(request,"addowner.html",{"form":form,"msg":msg})
    return render(request,"addowner.html",{"form":form,"msg":msg})  

def deleteowner(request):
    return render(request,"deleteowner.html")  

def updateowner(request):
    return render(request,"updateowner.html")  

def viewowners(request):
    return render(request,"viewowners.html")  






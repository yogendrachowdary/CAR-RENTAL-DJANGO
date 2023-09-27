from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q


from resadmin.models import Admin


# Create your views here.

def adminhome(request):
    return render(request, "adminhome.html")

def changepassword(request):
    return render(request, "changepassword.html")

def admincustomer(request):
    return render(request, "admincustomer.html")

def admincar(request):
    return render(request, "admincar.html")

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


        

    
    





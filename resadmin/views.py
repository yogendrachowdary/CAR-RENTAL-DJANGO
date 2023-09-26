from django.shortcuts import render


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


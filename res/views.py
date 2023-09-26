from django.http import HttpResponse
from django.shortcuts import render


def demofunction(request):
    return HttpResponse("Hii this is a HTTP response")
def demofunction1(request):
    return HttpResponse("Hii this is a HTTP response 2")
def demofunction2(request):
    return HttpResponse("Hii this is a HTTP response 3")
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"login.html")
def contactus(request):
    return render(request,"contactus.html")


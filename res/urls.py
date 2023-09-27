"""
URL configuration for res project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),       #this means if you type /admin you will be redirected to admin console
    path("", views.demofunction,name="demo"),
    path("demo1", views.demofunction1,name="demo"),
    path("demo2", views.demofunction2, name="demo"),  #1.url 2.function name 3. name
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("login", views.login, name="login"),
    path("contactus", views.contactus, name="contactus"),
    path("",include("resadmin.urls")),  #this will check for urls in resadmin app's urls.py
    # path("",include("resowner.urls")),
    # path("",include("resuser.urls")),

]

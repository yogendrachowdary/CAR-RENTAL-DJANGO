from django.urls import path
from . import views

urlpatterns = [

        path("adminhome",views.adminhome,name="adminhome"),
        path("changepassword", views.changepassword, name="changepassword"),
        path("admincustomer", views.admincustomer, name="admincustomer"),
        path("admincar", views.admincar, name="admincar"),
        path("adminlgout", views.adminlogout, name="adminlogout"),

]

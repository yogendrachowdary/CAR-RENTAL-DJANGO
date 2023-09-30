from django.urls import path
from . import views

urlpatterns = [

        path("adminhome",views.adminhome,name="adminhome"),
        path("changepassword", views.changepassword, name="changepassword"),
        path("viewcustomers", views.viewcustomers, name="viewcustomers"),
        path("viewcars", views.viewcars, name="viewcars"),
        path("admincars", views.admincars, name="admincars"),
        path("addcar", views.addcar, name="addcar"),
        path("deletecar", views.deletecar, name="deletecar"),
        path("updatecar", views.updatecar, name="updatecar"),
        path("admincustomers", views.admincustomers, name="admincustomers"),
        path("addcustomer", views.addcustomer, name="addcustomer"),
        path("deletecustomer", views.deletecustomer, name="deletecustomer"),
        path("customerdeletion/<int:cid>", views.customerdeletion, name="customerdeletion"),
        path("updatecustomer", views.updatecustomer, name="updatecustomer"),
        path("customerupdation/<int:cid>", views.customerupdation, name="customerupdation"),
        path("adminlgout", views.adminlogout, name="adminlogout"),
        path("checkadminlogin", views.checkadminlogin, name="checkadminlogin"),
        path("adminowners", views.adminowners, name="adminowners"),
        path("addowner", views.addowner, name="addowner"),
        path("deleteowner", views.deleteowner, name="deleteowner"),
        path("updateowner", views.updateowner, name="updateowner"),
        path("viewowners", views.viewowners, name="viewowners"),






]

from django.contrib import admin
from .models import Customer,Car,Admin

# Register your models here.

admin.site.register(Admin)
admin.site.register(Customer)
admin.site.register(Car)

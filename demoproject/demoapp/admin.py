from django.contrib import admin
from .models import MenuCategory, Menu, Customer,Vehicle
# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Customer)
admin.site.register(Vehicle)
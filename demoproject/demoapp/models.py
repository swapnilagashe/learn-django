from django.db import models
from unicodedata import name
# Create your models here.
class MenuCategory(models.Model):
    category = models.CharField(max_length=100)
    
class Menu(models.Model):
    item_name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.IntegerField()
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT,default = None,related_name = "category_name")
    
    def __str__(self):
        return self.name+" : " + self.cuisine
    
class Customer(models.Model): 
    name = models.CharField(max_length=255) 

class Vehicle(models.Model): 
    name = models.CharField(max_length=255) 
    customer = models.ForeignKey( 
        Customer, 
        on_delete=models.CASCADE, 
        related_name='Vehicle' 
    ) 
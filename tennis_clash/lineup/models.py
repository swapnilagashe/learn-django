from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=25)
    level = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
    serve = models.IntegerField(default=0)
    volley = models.IntegerField(default=0)
    forehand = models.IntegerField(default=0)
    backhand = models.IntegerField(default=0)
    
class Racket(models.Model):
    name = models.CharField(max_length=20)
    level =models.IntegerField(default=0)

class Grip(models.Model):
    name = models.CharField(max_length=20)
    level =models.IntegerField(default=0)
    
class Shoes(models.Model):
    name = models.CharField(max_length=20)
    level =models.IntegerField(default=0)
    
class Wristband(models.Model):
    name = models.CharField(max_length=20)
    level =models.IntegerField(default=0)
    
class Nutrition(models.Model):
    name = models.CharField(max_length=20)
    level =models.IntegerField(default=0)
    
class Workout(models.Model):
    name = models.CharField(max_length=20)
    level =models.IntegerField(default=0)
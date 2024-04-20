from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from lineup import views

app_name='lineup' 
urlpatterns = [
    path('',views.index)
    #re_path(r're_path', views.x)

]
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.form_view),
    path('', views.index,name='index'),
]

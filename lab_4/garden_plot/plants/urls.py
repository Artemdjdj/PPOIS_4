from django.contrib import admin
from django.urls import path
from . import views

app_name = 'plants'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_plant', views.add_plant, name="add_plant")
]

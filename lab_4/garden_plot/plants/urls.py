from django.contrib import admin
from django.urls import path
from . import views

app_name = "plants"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_plant/", views.add_plant, name="add_plant"),
    path("delete_plant/<int:plant_id>/", views.delete_plant, name="delete_plant"),
    path("water_plant/<int:plant_id>/", views.water_plant, name="water_plant"),
]

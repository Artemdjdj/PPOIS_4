from django.contrib import admin
from django.urls import path
from . import views

app_name = "recreation_area"

urlpatterns = [
    path("", views.index, name="index"),
    path("grill/", views.grill, name="grill"),
    path("create_grill/", views.create_grill, name="create_grill"),
    path("delete_grill/", views.delete_grill, name="delete_grill"),
    path("add_recreation_area/", views.add_recreation_area, name="add_recreation_area"),
    path(
        "delete_recreation_area/",
        views.delete_recreation_area,
        name="delete_recreation_area",
    ),
    path(
        "recreation_area_info/", views.recreation_area_info, name="recreation_area_info"
    ),
    path("add_fitting/", views.add_fitting, name="add_fitting"),
    path(
        "delete_fitting/<int:fitting_id>/", views.delete_fitting, name="delete_fitting"
    ),
]

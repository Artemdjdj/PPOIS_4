from django.contrib import admin
from django.urls import path
from . import views

app_name = 'recreation_area'

urlpatterns = [
    path('', views.index, name="index"),
    path('grill/', views.grill, name="grill"),
    path('create_grill/', views.create_grill, name="create_grill"),
    path('delete_grill/', views.delete_grill, name="delete_grill"),
]

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'recreation_area'

urlpatterns = [
    path('', views.index, name="index"),
    path('grill', views.grill, name="grill"),
]

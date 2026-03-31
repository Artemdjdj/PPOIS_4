from django.contrib import admin
from django.urls import path
from . import views

app_name = 'irrigation_system'

urlpatterns = [
    path('', views.index, name="index"),
    path('activate/', views.activate, name="activate"),
    path('deactivate/', views.deactivate, name="deactivate"),
]

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'plot'

urlpatterns = [
    path('', views.plot_info, name="plot_info"),
    path('add_plot/', views.add_plot, name="add_plot"),
    path('delete_plot/', views.delete_plot, name="delete_plot"),
    path('soil_info/', views.soil_info, name="soil_info"),
]

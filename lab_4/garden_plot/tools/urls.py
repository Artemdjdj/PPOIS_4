from django.contrib import admin
from django.urls import path
from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.index, name="index"),
    path('add_tool/', views.add_tool, name="add_tool"),
    path('delete_tool/<int:tool_id>/', views.delete_tool, name="delete_tool"),
    path('use_tool/<int:tool_id>/', views.use_tool, name="use_tool"),
    path('maintain_tool/<int:tool_id>/', views.maintain_tool, name="maintain_tool"),
]

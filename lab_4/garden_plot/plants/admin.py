from django.contrib import admin
from .models import ColorModel, PlantModel

class ColorModelAdmin(admin.ModelAdmin):
    prepopulated_fields  = {'slug':('name',)}
    list_display=['name', 'slug']
    search_fields=['name', 'slug']

class PlantModelAdmin(admin.ModelAdmin):
    list_display = ['height','name', 'get_color', 'is_watered']
    search_fields = ['name', 'get_color', 'is_watered']

admin.site.register(ColorModel, ColorModelAdmin)
admin.site.register(PlantModel, PlantModelAdmin)
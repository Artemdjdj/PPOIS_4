from django.contrib import admin
from .models import FittingModel

class FittingModelAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name']


admin.site.register(FittingModel, FittingModelAdmin)
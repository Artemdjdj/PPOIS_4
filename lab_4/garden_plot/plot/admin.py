from django.contrib import admin
from .models import SoilModel, PlotModel


class SoilModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]


class PlotModelAdmin(admin.ModelAdmin):
    list_display = ["square", "perimeter", "soil_name"]
    search_fields = ["soil_name", "square", "perimeter"]


admin.site.register(SoilModel, SoilModelAdmin)
admin.site.register(PlotModel, PlotModelAdmin)

from django.contrib import admin

from .models import IrrigationSystemModel


class IrrigationSystemModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "is_active", "time_of_last_adding_water"]
    search_fields = ["pk", "is_active"]


admin.site.register(IrrigationSystemModel, IrrigationSystemModelAdmin)

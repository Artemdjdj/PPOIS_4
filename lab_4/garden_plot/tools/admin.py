from django.contrib import admin
from .models import ToolTypeModel, ToolStateModel, ToolModel


class ToolTypeModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]


class ToolStateModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]


class ToolModelAdmin(admin.ModelAdmin):
    list_display = [
        "tool_type_name",
        "brand",
        "usage_count",
        "state_name",
        "date_of_maintain",
    ]
    search_fields = ["brand"]


admin.site.register(ToolTypeModel, ToolTypeModelAdmin)
admin.site.register(ToolStateModel, ToolStateModelAdmin)
admin.site.register(ToolModel, ToolModelAdmin)

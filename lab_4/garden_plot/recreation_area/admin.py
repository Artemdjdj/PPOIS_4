from django.contrib import admin
from .models import FittingModel, MeatTypeModel, GrillModel, RecreationAreaModel


class FittingModelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


class MeatTypeModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]


class GrillModelAdmin(admin.ModelAdmin):
    list_display = ["pk"]
    search_fields = ["pk"]


class RecreationAreaModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "is_clean"]
    search_fields = ["pk", "is_clean"]


admin.site.register(FittingModel, FittingModelAdmin)
admin.site.register(MeatTypeModel, MeatTypeModelAdmin)
admin.site.register(GrillModel, GrillModelAdmin)
admin.site.register(RecreationAreaModel, RecreationAreaModelAdmin)

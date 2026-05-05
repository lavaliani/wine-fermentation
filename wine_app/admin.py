from django.contrib import admin

from .models import FermentationEntry, WineProject


class FermentationEntryInline(admin.TabularInline):
    model = FermentationEntry
    extra = 0
    fields = ("measured_at", "temperature", "brix", "sugar", "ph", "acidity", "action")


@admin.register(WineProject)
class WineProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "grape_type", "wine_style", "harvest_date", "is_active", "created_at")
    list_filter = ("wine_style", "is_active", "created_at")
    search_fields = ("name", "grape_type", "vessel")
    inlines = [FermentationEntryInline]


@admin.register(FermentationEntry)
class FermentationEntryAdmin(admin.ModelAdmin):
    list_display = ("project", "measured_at", "temperature", "brix", "ph", "acidity")
    list_filter = ("measured_at",)
    search_fields = ("project__name", "action", "comment")

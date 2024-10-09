from django.contrib import admin

from .models import Ad, Category

class AdAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "description",
        "category",
        "phone",
        "owner",
        "condition",
    ]
    list_display_links = ["title"]
    list_editable = ["category"]
    list_filter = ["category"]


admin.site.register(Ad, AdAdmin)
admin.site.register(Category)
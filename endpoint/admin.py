from django.contrib import admin

from endpoint.models import Cloth


class ClothAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_title": ("title",)}


admin.site.register(Cloth, ClothAdmin)
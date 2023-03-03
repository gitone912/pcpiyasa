from django.contrib import admin
from .models import RAM

@admin.register(RAM)
class RamAdmin(admin.ModelAdmin):
    list_display = ('ram_name', 'ram_brand', 'ram_size', 'ram_type', 'ram_cas_latency')
    list_filter = ('ram_brand', 'ram_type')
    search_fields = ('ram_name',)

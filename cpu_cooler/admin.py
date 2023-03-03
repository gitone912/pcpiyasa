from django.contrib import admin
from .models import cpu_cooler

@admin.register(cpu_cooler)
class cpu_coolerAdmin(admin.ModelAdmin):
    list_display = ('id', 'cpu_cooler_name', 'cpu_cooler_brand', 'cpu_cooler_model', 'cpu_cooler_fan_rpm', 'cpu_cooler_noise_level', 'cpu_cooler_color', 'cpu_cooler_price')
    list_filter = ('cpu_cooler_brand', 'cpu_cooler_fan_rpm', 'cpu_cooler_noise_level', 'cpu_cooler_color')
    search_fields = ('cpu_cooler_name', 'cpu_cooler_brand', 'cpu_cooler_model')
    ordering = ('id',)

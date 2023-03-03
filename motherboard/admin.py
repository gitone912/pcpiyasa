from django.contrib import admin
from .models import Motherboard

class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'motherboard_name', 'motherboard_brand', 'motherboard_model', 'motherboard_chipset')
    list_filter = ('motherboard_brand', 'motherboard_chipset')
    search_fields = ('motherboard_name', 'motherboard_brand', 'motherboard_model', 'motherboard_chipset')

admin.site.register(Motherboard, MotherboardAdmin)

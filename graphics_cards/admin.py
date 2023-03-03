from django.contrib import admin
from .models import GraphicsCard


@admin.register(GraphicsCard)
class GraphicsCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'graphic_card_name', 'graphic_card_brand')
    list_filter = ('graphic_card_brand', 'graphic_card_memory_interface', 'graphic_card_chipset')
    search_fields = ('graphic_card_name', 'graphic_card_brand', 'graphic_card_model', 'graphic_card_chipset')
    ordering = ('id',)
    fieldsets = (
        ('General', {
            'fields': ('graphic_card_name', 'graphic_card_brand', 'graphic_card_model')
        }),
        ('Details', {
            'fields': ('graphic_card_memory', 'graphic_card_memory_interface', 'graphic_card_length', 'graphic_card_interface', 'graphic_card_chipset', 'graphic_card_base_clock', 'graphic_card_clock_speed', 'graphic_card_frame_sync')
        }),
        ('Image', {
            'fields': ('graphic_card_image_url',)
        })
    )

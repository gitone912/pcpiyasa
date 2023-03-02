from django.contrib import admin

from .models import *
from django.utils.html import format_html

@admin.register(processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ("id", "display_image", "processor_name", "processor_brand")

    def display_image(self, obj):  # sourcery skip: use-fstring-for-formatting
        return format_html('<img src="{}" width="40"/>'.format(obj.processor_image_url))
    display_image.short_description = 'Image'
    
    
admin.site.register(pc_builder_class)

@admin.register(product_added)
class product_added(admin.ModelAdmin):
    list_display = ("user", "processor")
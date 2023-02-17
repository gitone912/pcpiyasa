from django.contrib import admin

from .models import *
@admin.register(processor)
class processor(admin.ModelAdmin):
    list_display = ("id", "processor_name","processor_brand")
admin.site.register(pc_builder_class)

@admin.register(product_added)
class product_added(admin.ModelAdmin):
    list_display = ("user", "processor")
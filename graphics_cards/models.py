from django.db import models

# Create your models here.
import uuid
from django.db import models

class GraphicsCard(models.Model):
    id = models.AutoField(primary_key=True)
    Image_URL = models.URLField(max_length=500 , blank=True , null=True)
    graphics_card_old_url = models.CharField( max_length=150 , blank=True , null=True)
    graphic_card_name = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_brand = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_model = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_memory = models.CharField(max_length=200)
    graphic_card_memory_interface = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_length = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_interface = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_chipset = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_base_clock = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_clock_speed = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_frame_sync = models.CharField(max_length=200 , blank=True , null=True)
    graphic_card_image_url = models.URLField(max_length=500 , blank=True , null=True)
    
    def __str__(self):
        return self.graphic_card_name

from django.db import models
from processors.models import processor
from cpu_cooler.models import cpu_cooler
from django.contrib.auth.models import User
from motherboard.models import *
from ram.models import *
from graphics_cards.models import *
from motherboard.models import Motherboard
from graphics_cards.models import GraphicsCard

# Create your models here.
class pc_builder_class(models.Model):
    processor = models.ForeignKey(processor, on_delete=models.CASCADE)
    cpu_cooler = models.ForeignKey(cpu_cooler, on_delete=models.CASCADE,null=True,blank=True)
    
class processor_added(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    processor = models.ForeignKey(processor, on_delete=models.CASCADE,null=True,blank=True)
    exists = models.BooleanField(default=False)
    
class cpu_cooler_added(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    cpu_cooler = models.ForeignKey(cpu_cooler, on_delete=models.CASCADE,null=True,blank=True)
    exists = models.BooleanField(default=False)
    
class RAM_added(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE,null=True,blank=True)
    exists = models.BooleanField(default=False)
    
class motherboard_added(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE,null=True,blank=True)
    exists = models.BooleanField(default=False)
    
class graphics_card_added(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    graphics_card = models.ForeignKey(GraphicsCard, on_delete=models.CASCADE,null=True,blank=True)
    exists = models.BooleanField(default=False)
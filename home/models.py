from django.db import models
from processors.models import processor
from cpu_cooler.models import cpu_cooler
from django.contrib.auth.models import User
from motherboard.models import *
from ram.models import *
from graphics_cards.models import *
# Create your models here.
class pc_builder_class(models.Model):
    processor = models.ForeignKey(processor, on_delete=models.CASCADE)
    cpu_cooler = models.ForeignKey(cpu_cooler, on_delete=models.CASCADE,null=True,blank=True)
    
class product_added(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    processor = models.ForeignKey(processor, on_delete=models.CASCADE,null=True,blank=True)
    cpu_cooler = models.ForeignKey(cpu_cooler, on_delete=models.CASCADE,null=True,blank=True)
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class processor(models.Model):
    id = models.AutoField(primary_key=True)
    processor_name = models.CharField(max_length=200 , null=False)
    processor_short_name = models.CharField(max_length=200 , null=False)
    processor_brand = models.CharField(max_length=200)
    processor_url = models.CharField( max_length=200)
    processor_core_count = models.CharField(max_length=200)
    processor_performance_core_clock= models.CharField(max_length=200)
    processor_performance_boost_clock= models.CharField(max_length=200,null=True,blank=True)
    processor_integrated_graphics = models.CharField(max_length=200)
    processor_tdp = models.CharField(max_length=200)
    processor_smt = models.CharField(max_length=200)
    processor_price = models.CharField(max_length=200)
    processor_image_url = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
    
class pc_builder_class(models.Model):
    processor = models.ForeignKey(processor, on_delete=models.CASCADE)
    
    
class product_added(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE,null=True,blank=True)
    processor = models.ForeignKey(processor, on_delete=models.CASCADE,null=True,blank=True)
    
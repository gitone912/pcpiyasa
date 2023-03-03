import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cpu_cooler(models.Model):
    id = models.AutoField(primary_key=True)
    cpu_cooler_name = models.CharField(max_length=200, null=False)
    cpu_cooler_brand = models.CharField(max_length=200)
    cpu_cooler_model = models.CharField(max_length=200)
    cpu_cooler_fan_rpm = models.CharField(max_length=200)
    cpu_cooler_noise_level = models.CharField(max_length=200)
    cpu_cooler_color = models.CharField(max_length=200)
    cpu_cooler_price = models.CharField(max_length=200)
    cpu_cooler_image_url = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.id)
    
    
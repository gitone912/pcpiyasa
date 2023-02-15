import uuid
from django.db import models

# Create your models here.
class new_processor(models.Model):
    id = models.AutoField(primary_key=True)
    processor_brand = models.CharField(max_length=200)
    processor_cores = models.CharField(max_length=200)
    processor_image_alt = models.CharField(max_length=200)
    processor_image_url = models.CharField( max_length=200)
    processor_model = models.CharField(max_length=200)
    processor_name = models.CharField(max_length=200 , null=False)
    processor_socket_type = models.CharField(max_length=200)
    processor_speed = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)
    
class pc_builder_class(models.Model):
    processor = models.ForeignKey(new_processor, on_delete=models.CASCADE)
    prod_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=200)
    
class product_added(models.Model):
    processor = models.ForeignKey(new_processor, on_delete=models.CASCADE)
    

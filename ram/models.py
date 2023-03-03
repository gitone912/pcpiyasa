from django.db import models

class RAM(models.Model):
    ram_image_url = models.URLField()
    ram_name = models.CharField(max_length=200)
    ram_old_url = models.URLField()
    ram_brand = models.CharField(max_length=50)
    ram_model = models.CharField(max_length=50)
    ram_size = models.CharField(max_length=10)
    ram_quantity = models.CharField(max_length=20)
    ram_type = models.CharField(max_length=10)
    Field8 = models.CharField(max_length=20)
    ram_dimm_type = models.CharField(max_length=20)
    ram_cas_latency = models.CharField(max_length=10)

    def __str__(self):
        return self.ram_name

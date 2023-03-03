from django.db import models

class Motherboard(models.Model):
    motherboard_image_url = models.URLField(max_length=500)
    motherboard_name = models.CharField(max_length=200)
    motherboard_old_link = models.URLField(max_length=500)
    motherboard_brand = models.CharField(max_length=200)
    motherboard_model = models.CharField(max_length=200)
    motherboard_chipset = models.CharField(max_length=200)
    motherboard_form_factor = models.CharField(max_length=200)
    motherboard_socket_type = models.CharField(max_length=200)
    motherboard_memory_slot = models.CharField(max_length=200)
    motherboard_max_memory_support = models.CharField(max_length=200)

    def __str__(self):
        return self.motherboard_name

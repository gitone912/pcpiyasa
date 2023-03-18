
from django.db import models
from django.contrib.auth.models import User

class user_details(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class GeneralPreferences(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='general_preferences')
    # add any general preferences fields you want here

class EmailAndPassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='email_and_password')
    # add any email and password fields you want here

class Notifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='notifications')
    # add any notification fields you want here

class MerchantsAndPricing(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='merchants_and_pricing')
    # add any merchant and pricing fields you want here

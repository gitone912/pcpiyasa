from rest_framework import serializers
from .models import *

class RAM_serializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'
from rest_framework import serializers
from .models import *

class cpu_cooler_serializer(serializers.ModelSerializer):
    class Meta:
        model = cpu_cooler
        fields = '__all__'
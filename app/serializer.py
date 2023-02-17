from rest_framework import serializers
from .models import *

class processor_serializer(serializers.ModelSerializer):
    class Meta:
        model = processor
        fields = '__all__'
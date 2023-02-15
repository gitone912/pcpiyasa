from rest_framework import serializers
from .models import *

class processor_serializer(serializers.ModelSerializer):
    class Meta:
        model = new_processor
        fields = '__all__'
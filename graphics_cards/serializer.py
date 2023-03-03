from rest_framework import serializers
from .models import *

class graphics_card_serializer(serializers.ModelSerializer):
    class Meta:
        model = GraphicsCard
        fields = '__all__'
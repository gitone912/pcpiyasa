from rest_framework import serializers
from .models import *

class Mother_board_serializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = '__all__'
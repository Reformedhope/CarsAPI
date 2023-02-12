from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta: # This is where we define small bits of informaion about this car Serializer class
        model = Car
        fields = ['id','make','model','year','price']

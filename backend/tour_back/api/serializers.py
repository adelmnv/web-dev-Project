from rest_framework import serializers
from .models import Country, City, MealType, Flight, Hotel, Tour, Image

# class CountrySerializer(serializers.Serializer):
    

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country']
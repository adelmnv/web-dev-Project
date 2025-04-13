from rest_framework import serializers
from .models import Application, City, Flight, Hotel, Tour, Image

class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.ImageField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    

class MealTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'country', 'image', 'created_at', 'updated_at']


class FlightSerializer(serializers.ModelSerializer):
    origin_id = serializers.IntegerField()
    destination_id = serializers.IntegerField()
    class Meta:
        model = Flight
        fields = ['id', 'airline', 'flight_number', 'departure', 'arrival','origin_id', 'destination_id', 'icon', 'created_at', 'updated_at']


class HotelSerializer(serializers.ModelSerializer):
    city_id = serializers.IntegerField()
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'city_id', 'address', 'rating', 'created_at', 'updated_at']


class TourSerializer(serializers.ModelSerializer):
    hotel_id = serializers.IntegerField()
    flight_id = serializers.IntegerField()
    meal_type_id = serializers.IntegerField()
    class Meta:
        model = Tour
        fields = ['id', 'name', 'hotel_id', 'flight_id', 'price', 'meal_type_id', 'start_date', 'end_date', 'created_at', 'updated_at']


class ImageSerializer(serializers.ModelSerializer):
    tour_id = serializers.IntegerField()
    class Meta:
        model = Image
        fields = ['id', 'image', 'tour_id', 'created_at', 'updated_at']

class ApplicationSerializer(serializers.ModelSerializer):
    tour_id = serializers.IntegerField()
    class Meta:
        model = Application
        fields = ['id', 'name', 'email', 'phone', 'tour_id','status', 'created_at', 'updated_at']

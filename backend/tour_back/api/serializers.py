from rest_framework import serializers
from .models import Application, City, Flight, Hotel, Tour, Country 

class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    image = serializers.CharField(allow_null=True, required=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    

class MealTypeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField()
    description = serializers.CharField(allow_null=True, required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return super().create(validated_data)
    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)
        instance.save()
        return instance


class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField()
    class Meta:
        model = City
        fields = ['id', 'name', 'country_id', 'images', 'created_at', 'updated_at']


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
        fields = ['id', 'name', 'city_id', 'address', 'rating','description', 'images', 'created_at', 'updated_at'] 


class TourSerializer(serializers.ModelSerializer):
    hotel_id = serializers.IntegerField()
    meal_type_id = serializers.IntegerField()
    class Meta:
        model = Tour
        fields = ['id', 'name', 'hotel_id', 'price', 'meal_type_id', 'duration', 'created_at', 'updated_at']

class ApplicationSerializer(serializers.ModelSerializer):
    tour_id = serializers.IntegerField()
    flights_to = serializers.PrimaryKeyRelatedField(many=True, queryset=Flight.objects.all())  # Many-to-Many field
    flights_back = serializers.PrimaryKeyRelatedField(many=True, queryset=Flight.objects.all())  # Many-to-Many field
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # Read-only field

    class Meta:
        model = Application
        fields = [
            'id', 'name', 'email', 'phone', 'tour_id', 'flights_to', 'flights_back',
            'total_price', 'status', 'created_at', 'updated_at'
        ]

class CustomRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['name', 'email', 'message', 'created_at', 'updated_at']
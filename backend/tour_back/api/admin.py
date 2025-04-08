from django.contrib import admin
from api.models import Application, Country, City, Image, MealType, Flight, Hotel, Tour

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'created_at', 'updated_at')
    search_fields = ('name', 'country__name')

@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    search_fields = ('type',)

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'airline', 'flight_number', 'departure', 'arrival', 'origin', 'destination','icon', 'created_at', 'updated_at')
    search_fields = ('airline', 'flight_number', 'origin__name', 'destination__name')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'rating', 'created_at', 'updated_at')
    search_fields = ('name', 'city__name', 'address')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hotel', 'flight', 'price', 'meal_type', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('name',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'tour')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'tour','status', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone', 'tour_id')

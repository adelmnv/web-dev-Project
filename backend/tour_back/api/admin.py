from django.contrib import admin
from api.models import Application, Country, City, CustomRequest, MealType, Flight, Hotel, Tour

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','image', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_display_links = ('id', 'name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country','images', 'created_at', 'updated_at')
    search_fields = ('name', 'country__name')
    list_display_links = ('id', 'name')

@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    search_fields = ('type',)
    list_display_links = ('id', 'type')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'airline', 'flight_number', 'departure', 'arrival', 'origin', 'destination','icon', 'created_at', 'updated_at')
    search_fields = ('airline', 'flight_number', 'origin__name', 'destination__name')
    list_display_links = ('id', 'airline')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address', 'rating','images', 'created_at', 'updated_at')
    search_fields = ('name', 'city__name', 'address')
    list_display_links = ('id', 'name')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hotel', 'flight', 'price', 'meal_type', 'start_date', 'end_date','images', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_display_links = ('id', 'name')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'tour','status', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone', 'tour_id')
    list_display_links = ('id', 'name')

@admin.register(CustomRequest)
class CustomRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message', 'created_at', 'updated_at')
    search_fields = ('name', 'email')
    list_display_links = ('id', 'name')

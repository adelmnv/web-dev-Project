from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class MealType(models.Model):
    type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.type


class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flights_from')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='flights_to')
    icon = models.ImageField(upload_to='flight_icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.airline} {self.flight_number}: {self.origin.name} to {self.destination.name}"
    
    def clean(self):
        if self.departure >= self.arrival:
            raise ValidationError("Departure time must be before arrival time.")


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    address = models.CharField(max_length=255)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.name}, {self.city.name}"

   
class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tours')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='tours')
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE, related_name='tours')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.name} ({self.start_date} - {self.end_date})"

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
    
    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")


class Image(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tour_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"Image for {self.tour.name}"
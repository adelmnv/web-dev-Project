from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Application, Country, City, CustomRequest, Flight, Hotel, Tour, MealType
from .serializers import ApplicationSerializer, CountrySerializer, CitySerializer, CustomRequestSerializer, FlightSerializer, HotelSerializer, TourSerializer, MealTypeSerializer

@api_view(http_method_names=['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def country_detail(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def meal_type_list(request):
    if request.method == 'GET':
        meal_types = MealType.objects.all()
        serializer = MealTypeSerializer(meal_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MealTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def meal_type_detail(request, meal_type_id):
    try:
        meal_type = MealType.objects.get(id=meal_type_id)
    except MealType.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MealTypeSerializer(meal_type)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MealTypeSerializer(instance=meal_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        meal_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(http_method_names=['GET', 'POST'])
# def image_list(request):
#     if request.method == 'GET':
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# def image_detail(request, image_id):
#     try:
#         image = Image.objects.get(id=image_id)
#     except Image.DoesNotExist as e:
#         return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ImageSerializer(image)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = ImageSerializer(instance=image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class CityList(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetail(APIView):
    def get_object(self, city_id):
        try:
            return City.objects.get(id=city_id)
        except City.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, city_id):
        city = self.get_object(city_id)
        serializer = CitySerializer(city)
        return Response(serializer.data)
    
    def put(self, request, city_id):
        city = self.get_object(city_id)
        serializer = CitySerializer(instance=city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, city_id):
        city = self.get_object(city_id)
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class FlightList(APIView):
    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlightDetail(APIView):
    def get_object(self, flight_id):
        try:
            return Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, flight_id):
        flight = self.get_object(flight_id)
        serializer = FlightSerializer(flight)
        return Response(serializer.data)
    
    def put(self, request, flight_id):
        flight = self.get_object(flight_id)
        serializer = FlightSerializer(instance=flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, flight_id):
        flight = self.get_object(flight_id)
        flight.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HotelList(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HotelDetail(APIView):
    def get_object(self, hotel_id):
        try:
            return Hotel.objects.get(id=hotel_id)
        except Hotel.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, hotel_id):
        hotel = self.get_object(hotel_id)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    
    def put(self, request, hotel_id):
        hotel = self.get_object(hotel_id)
        serializer = HotelSerializer(instance=hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, hotel_id):
        hotel = self.get_object(hotel_id)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TourList(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TourDetail(APIView):
    def get_object(self, tour_id):
        try:
            return Tour.objects.get(id=tour_id)
        except Tour.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, tour_id):
        tour = self.get_object(tour_id)
        serializer = TourSerializer(tour)
        return Response(serializer.data)
    
    def put(self, request, tour_id):
        tour = self.get_object(tour_id)
        serializer = TourSerializer(instance=tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, tour_id):
        tour = self.get_object(tour_id)
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ImageList(APIView):
#     def get(self, request):
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ImageDetail(APIView):
#     def get_object(self, image_id):
#         try:
#             return Image.objects.get(id=image_id)
#         except Image.DoesNotExist as e:
#             return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, image_id):
#         image = self.get_object(image_id)
#         serializer = ImageSerializer(image)
#         return Response(serializer.data)
    
#     def put(self, request, image_id):
#         image = self.get_object(image_id)
#         serializer = ImageSerializer(instance=image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, image_id):
#         image = self.get_object(image_id)
#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class ApplicationList(APIView):
    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationDetail(APIView):
    def get_object(self, application_id):
        try:
            return Application.objects.get(id=application_id)
        except Application.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, application_id):
        application = self.get_object(application_id)
        serializer = ApplicationSerializer(application)
        return Response(serializer.data)
    
    def put(self, request, application_id):
        application = self.get_object(application_id)
        serializer = ApplicationSerializer(instance=application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, application_id):
        application = self.get_object(application_id)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CustomRequestList(APIView):
    def get(self, request):
        custom_requests = CustomRequest.objects.all()
        serializer = CustomRequestSerializer(custom_requests, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomRequestDetail(APIView):
    def get_object(self, request_id):
        try:
            return CustomRequest.objects.get(id=request_id)
        except CustomRequest.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, request_id):
        custom_request = self.get_object(request_id)
        serializer = CustomRequestSerializer(custom_request)
        return Response(serializer.data)
    
    def put(self, request, request_id):
        custom_request = self.get_object(request_id)
        serializer = CustomRequestSerializer(instance=custom_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, request_id):
        custom_request = self.get_object(request_id)
        custom_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
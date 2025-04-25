from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from api.models import Flight
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Application, Country, City, CustomRequest, Flight, Hotel, Tour, MealType
from .serializers import (
    ApplicationSerializer,
    CountrySerializer,
    CitySerializer,
    CustomRequestSerializer,
    FlightSerializer,
    HotelSerializer,
    TourSerializer,
    MealTypeSerializer,
)

@api_view(http_method_names=['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required for POST requests.'}, status=status.HTTP_403_FORBIDDEN)
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
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required for POST requests.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required for POST requests.'}, status=status.HTTP_403_FORBIDDEN)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def meal_type_list(request):
    if request.method == 'GET':
        meal_types = MealType.objects.all()
        serializer = MealTypeSerializer(meal_types, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required for POST requests.'}, status=status.HTTP_403_FORBIDDEN)
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
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required for POST requests.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = MealTypeSerializer(instance=meal_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required for POST requests.'}, status=status.HTTP_403_FORBIDDEN)
        meal_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CityList(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    
    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    
    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    
    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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
    
    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get(self, request, tour_id):
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

class ApplicationList(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get(self, request):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()

        flights_to_data = data.pop('flights_to', [])
        flights_back_data = data.pop('flights_back', [])

        serializer = ApplicationSerializer(data=data)
        if serializer.is_valid():
            application = serializer.save()

            if flights_to_data:
                flights_to = Flight.objects.filter(id__in=flights_to_data)
                application.flights_to.set(flights_to)
            if flights_back_data:
                flights_back = Flight.objects.filter(id__in=flights_back_data)
                application.flights_back.set(flights_back)

            application.total_price = application.calculate_total_price()
            application.save()

            return Response(ApplicationSerializer(application).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationDetail(APIView):
    def get_object(self, application_id):
        try:
            return Application.objects.get(id=application_id)
        except Application.DoesNotExist as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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

class CustomRequestList(APIView):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [AllowAny()]

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
    
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return [IsAuthenticated()]
        return [AllowAny()]
    
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

@api_view(http_method_names=['GET'])
def find_flights(request):
    origin_id = request.GET.get('origin_id')
    destination_id = request.GET.get('destination_id')
    departure_date = request.GET.get('departure_date')
    return_date = request.GET.get('return_date')

    ##print(f"Origin ID: {origin_id}, Destination ID: {destination_id}, Departure Date: {departure_date}, Return Date: {return_date}")

    if not all([origin_id, destination_id, departure_date, return_date]):
        return JsonResponse({'error': 'All parameters: origin_id, destination_id, departure_date, return_date are required.'}, status=400)

    if departure_date >= return_date:
        return JsonResponse({'error': 'Departure date must be earlier than return date'}, status=400)

    try:
        flights_to = Flight.objects.filter(
            origin_id=origin_id,
            destination_id=destination_id,
            departure__date=departure_date
        )[:3]

        flights_back = Flight.objects.filter(
            origin_id=destination_id,
            destination_id=origin_id,
            departure__date=return_date
        )[:3]

        # Search for connecting flights
        if not flights_to.exists():
            connecting_flights_to = Flight.objects.filter(
                origin_id=origin_id,
                departure__date=departure_date
            ).exclude(destination_id=origin_id)

            connecting_flights_to = [
                {
                    'first_leg': first_leg,
                    'second_leg': second_leg
                }
                for first_leg in connecting_flights_to
                for second_leg in Flight.objects.filter(
                    origin_id=first_leg.destination_id,
                    destination_id=destination_id,
                    departure__date=departure_date
                )
                if first_leg.arrival < second_leg.departure
            ][:3]

        else:
            connecting_flights_to = []

        if not flights_back.exists():
            connecting_flights_back = Flight.objects.filter(
                origin_id=destination_id,
                departure__date=return_date
            ).exclude(destination_id=destination_id)

            connecting_flights_back = [
                {
                    'first_leg': first_leg,
                    'second_leg': second_leg
                }
                for first_leg in connecting_flights_back
                for second_leg in Flight.objects.filter(
                    origin_id=first_leg.destination_id,
                    destination_id=origin_id,
                    departure__date=return_date
                )
                if first_leg.arrival < second_leg.departure
            ][:3]

        else:
            connecting_flights_back = []


        ##print(f"Direct Flights to: {len(flights_to)}, Connecting Flights to: {len(connecting_flights_to)}")
        ##print(f"Direct Flights back: {len(flights_back)}, Connecting Flights back: {len(connecting_flights_back)}")

        flights_to_data = FlightSerializer(flights_to, many=True).data
        flights_back_data = FlightSerializer(flights_back, many=True).data

        connecting_flights_to_data = [
            {
                'first_leg': FlightSerializer(flight['first_leg']).data,
                'second_leg': FlightSerializer(flight['second_leg']).data
            }
            for flight in connecting_flights_to
        ]

        connecting_flights_back_data = [
            {
                'first_leg': FlightSerializer(flight['first_leg']).data,
                'second_leg': FlightSerializer(flight['second_leg']).data
            }
            for flight in connecting_flights_back
        ]

        return JsonResponse({
            'flights_to': flights_to_data,
            'connecting_flights_to': connecting_flights_to_data,
            'flights_back': flights_back_data,
            'connecting_flights_back': connecting_flights_back_data
        })

    except Exception as e:
        ##print(f"Error in find_flights: {str(e)}")
        return JsonResponse({'error': str(e)}, status=500)

@api_view(http_method_names=['GET'])
def find_tours(request):
    meal_type_id = request.GET.get('meal_type_id')
    duration = request.GET.get('duration')
    city_id = request.GET.get('city_id')

    if not any([meal_type_id, duration, city_id]):
        return JsonResponse({'error': 'At least one parameter (meal_type_id, duration, city_id) is required.'}, status=400)

    try:
        filters = {}
        if meal_type_id:
            filters['meal_type_id'] = meal_type_id
        if duration:
            filters['duration'] = duration
        if city_id:
            filters['hotel__city_id'] = city_id

        tours = Tour.objects.filter(**filters)

        serializer = TourSerializer(tours, many=True)
        return JsonResponse(serializer.data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

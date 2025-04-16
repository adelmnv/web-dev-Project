from django.urls import path
from api.views import ApplicationDetail, ApplicationList, country_list, country_detail, meal_type_list, meal_type_detail, FlightList, FlightDetail, HotelList, HotelDetail, TourList, TourDetail, ImageList, ImageDetail, LogoutView, CustomRequestList, CustomRequestDetail

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('countries/', country_list, name='country-list'),
    path('countries/<int:pk>/', country_detail, name='country-detail'),
    path('cities/', country_list, name='city-list'),
    path('cities/<int:pk>/', country_detail, name='city-detail'),
    path('meal-types/', meal_type_list, name='meal-type-list'),
    path('meal-types/<int:pk>/', meal_type_detail, name='meal-type-detail'),
    path('flights/', FlightList.as_view(), name='flight-list'),
    path('flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    path('hotels/', HotelList.as_view(), name='hotel-list'),
    path('hotels/<int:pk>/', HotelDetail.as_view(), name='hotel-detail'),
    path('tours/', TourList.as_view(), name='tour-list'),
    path('tours/<int:pk>/', TourDetail.as_view(), name='tour-detail'),
    path('images/', ImageList.as_view(), name='image-list'),
    path('images/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('applications/', ApplicationList.as_view(), name='application-list'),
    path('applications/<int:pk>/', ApplicationDetail.as_view(), name='application-detail'),
    path('custom-requests/', CustomRequestList.as_view(), name='custom-request-list'),
    path('custom-requests/<int:pk>/', CustomRequestDetail.as_view(), name='custom-request-detail'),

    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]

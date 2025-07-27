from django.urls import path, include
from hotel.views.hotel import HotelViewSet, RoomViewSet
from hotel.views.booking import RoomBookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'room-bookings', RoomBookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

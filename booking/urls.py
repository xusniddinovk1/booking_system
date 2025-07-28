from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..views import HotelVIewSet, RoomViewSet, RoomBookingViewSet, TransportViewSet, TransportBookingViewSet

router = DefaultRouter()
router.register(r'hotels', HotelVIewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'room-booking', RoomBookingViewSet)
router.register(r'transports', TransportViewSet)
router.register(r'transport-booking', TransportBookingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

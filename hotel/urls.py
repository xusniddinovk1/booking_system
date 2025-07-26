from django.urls import path, include
from hotel.views.hotel import HotelViewSet, RoomViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]

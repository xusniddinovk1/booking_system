from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from hotel.serializers.hotel import HotelSerializer, RoomSerializer
from ..models import Hotel, Room


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

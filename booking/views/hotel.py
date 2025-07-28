from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Hotel, Room
from ..permissions import IsOwnerOrReadOnly
from ..serializers import HotelSerializer, RoomSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

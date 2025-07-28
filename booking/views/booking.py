from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import RoomBooking
from ..permissions import IsOwnerOrReadOnly
from ..serializers import RoomBookingSerializer


class RoomBookingViewSet(viewsets.ModelViewSet):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

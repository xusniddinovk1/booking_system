from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import Transport, TransportBooking
from ..permissions import IsOwnerOrReadOnly
from ..serializers import TransportSerializer, TransportBookingSerializer


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]


class TransportBookingViewSet(viewsets.ModelViewSet):
    queryset = TransportBooking.objects.all()
    serializer_class = TransportBookingSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]

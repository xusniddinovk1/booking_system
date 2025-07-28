from rest_framework import viewsets
from ..models import Transport, TransportBooking
from ..serializers import TransportSerializer, TransportBookingSerializer


class TransportViewSet(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportBookingViewSet(viewsets.ModelViewSet):
    queryset = TransportBooking.objects.all()
    serializer_class = TransportBookingSerializer

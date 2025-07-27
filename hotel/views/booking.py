from rest_framework import viewsets
from ..models import RoomBooking
from ..serializers import RoomBookingSerializer


class RoomBookingViewSet(viewsets.ModelViewSet):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return RoomBooking.objects.all()
        return RoomBooking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

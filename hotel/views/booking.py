from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import RoomBooking
from ..serializers import RoomBookingSerializer


class RoomBookingViewSet(viewsets.ModelViewSet):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        if self.request.user.is_staff:
            return RoomBooking.objects.all()
        return RoomBooking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

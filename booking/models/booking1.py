from django.db import models
from custom_auth.models import CustomUser
from booking.models.hotel import Room

STATUS = (
    ('BOOKED', 'Booked'),
    ('COMPLETED', 'Completed'),
    ('CANCELED', 'Canceled')
)

BOOKED = 'Booked'
COMPLETED = 'Completed'
CANCELED = 'Canceled'


class RoomBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS, default=BOOKED)

    def __str__(self):
        return f'{self.user} booked {self.room}'

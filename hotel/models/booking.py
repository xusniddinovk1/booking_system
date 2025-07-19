from django.db import models
from user.models import CustomUser
from .hotel import Room


class RoomBooking(models.Model):
    BOOKED = 'Booked'
    CANCELED = 'Canceled'
    COMPLETED = 'Completed'

    STATUS = (
        ('BOOKED', 'Booked'),
        ('CANCELED', 'Canceled'),
        ('COMPLETED', 'Completed'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=15, choices=STATUS, default=BOOKED)

    def set_status(self, new_status):
        if new_status not in dict(self.STATUS):
            raise ValueError('Invalid Error')

        self.status = new_status
        self.save()

    def is_in_transition_allowed(self, new_status):
        allowed_transition = {
            self.BOOKED: [self.COMPLETED, self.CANCELED],
        }
        return new_status in allowed_transition.get(self.status, [])

    def __str__(self):
        return f'Booking 3{self.id} by {self.user}'

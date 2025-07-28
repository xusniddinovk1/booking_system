from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name


ROOM_TYPES = (
    ('SINGLE', 'Single'),
    ('DOUBLE', 'Double'),
    ('SUITE', 'Suite')
)


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveIntegerField()
    room_type = models.CharField(max_length=6, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

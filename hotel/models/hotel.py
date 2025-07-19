from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    rating = models.PositiveIntegerField()


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveIntegerField()
    room_type = models.CharField(max_length=10)
    price = models.IntegerField()

from django.db import models

from custom_auth.models import CustomUser


class Transport(models.Model):
    TRANSPORT_TYPE_CHOICES = (
        ('car', 'Car'),
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('plane', 'Plane'),
    )

    name = models.CharField(max_length=100)
    transport_type = models.CharField(max_length=20, choices=TRANSPORT_TYPE_CHOICES)
    capacity = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_transport_type_display()})"


class TransportBooking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='transport_bookings')
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.transport.name} ({self.start_date} to {self.end_date})"

    def total_days(self):
        return (self.end_date - self.start_date).days

    def total_price(self):
        return self.total_days() * self.transport.price_per_day

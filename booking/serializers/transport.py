from rest_framework import serializers
from ..models import Transport, TransportBooking


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ['id', 'name', 'transport_type', 'capacity', 'price_per_day']


class TransportBookingSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    total_days = serializers.SerializerMethodField()

    class Meta:
        model = TransportBooking
        fields = ['id', 'user', 'transport', 'start_date', 'end_date', 'total_days', 'total_price', 'is_paid', 'status',
                  'created_at']

    def get_total_price(self, obj):
        days = (obj.end_date - obj.start_date).days
        return days * obj.transport.price_per_day

    def get_total_days(self, obj):
        return max(1, (obj.end_date - obj.start_date).days)

    def validate(self, attrs):
        if attrs['start_date'] >= attrs['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return attrs

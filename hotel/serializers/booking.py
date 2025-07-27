from rest_framework import serializers
from ..models import RoomBooking


class RoomBookingSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    total_days = serializers.SerializerMethodField()

    class Meta:
        model = RoomBooking
        fields = ['id', 'user', 'room', 'check_in_date', 'check_out_date', 'is_paid', 'status', 'total_days', 'created_at', 'total_price']
        read_only_fields = ['user', 'status', 'created_at', 'total_days', 'total_price']

    def get_total_price(self, obj):
        nights = (obj.check_out_date - obj.check_in_date).days
        return nights * obj.room.price

    def get_total_days(self, obj):
        return (obj.check_out_date - obj.check_in_date).days

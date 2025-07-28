from rest_framework import serializers
from ..models import RoomBooking


class RoomBookingSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    total_days = serializers.SerializerMethodField()

    class Meta:
        model = RoomBooking
        fields = ['id', 'user', 'room', 'check_in_date', 'check_out_date', 'total_days', 'total_price', 'status']
        read_only_fields = ['user', 'status']

    def get_total_price(self, obj):
        days = (obj.check_out_date - obj.check_in_date).days
        return days * obj.room.price

    def get_total_days(self, obj):
        return (obj.check_out_date - obj.check_in_date).days

    def validate(self, attrs):
        check_in_date = attrs.get('check_in_date')
        check_out_date = attrs.get('check_out-date')

        if check_in_date and check_out_date and check_in_date >= check_out_date:
            raise serializers.ValidationError("Check-out date must be after check-in date.")

        return attrs

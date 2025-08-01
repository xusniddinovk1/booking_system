from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        user = authenticate(phone_number=phone_number, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')

        data['user'] = user
        return data

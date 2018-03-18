from rest_framework import serializers
from rest_framework.validators import ValidationError
from api_v0.models import Client, Driver, Tariff, Car, Order
import re


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'phone')

    def validate_phone(self, value):
        pattern = re.compile(r"^\+[0-9]{3}\ \([0-9]{2}\)\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}$")
        if pattern.match(value):
            return value
        raise ValidationError("Phone number should be like +998 (90) 111 11 11")

    def create(self, validated_data):
        phone = validated_data.pop('phone')

        return Client.objects.create(**validated_data)


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        # fields = ('id', 'name', 'description', 'driver', 'number')
        fields = '__all__'
    def validate_number(self, value):
        """
        There is two patterns of car number. Check it
        """
        pattern1 = re.compile(r"^[A-Z]{3}\ [0-9]{3}$")
        pattern2 = re.compile(r"^[A-Z]{2}\ [0-9]{3}\ [A-Z]{1}$")

        if pattern1.match(value) or pattern2.match(value):
            return value
        raise ValidationError("Car number should be like AAA 777 or AA 777 A")

    def create(self, validated_data):
        phone = validated_data.pop('number')

        return Client.objects.create(**validated_data)


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'name', 'cost_per_km')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'driver', 'tariff', 'car', 'start_taxiing_time', 'stop_taxiing_time')




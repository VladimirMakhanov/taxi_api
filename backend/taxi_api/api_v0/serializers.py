from rest_framework import serializers
from api_v0.models import Client, Driver, Tariff, Car, Order


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name')


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'description', 'driver')


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'name', 'cost_per_km')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'driver', 'tariff', 'car', 'start_taxiing_time', 'stop_taxiing_time')




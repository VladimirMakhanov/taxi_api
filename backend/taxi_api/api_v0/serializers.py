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

        # Start taxing time describe in model like `auto_now_add`, so exclude it
        # start_taxiing_time = serializers.DateTimeField(required=False)

        # This field should be written without user input
        stop_taxiing_time = serializers.DateTimeField(required=False, allow_null=True)

        fields = ('id', 'client', 'driver', 'tariff', 'car', 'stop_taxiing_time')

    def get_other_pending_orders_of_client(self, value):
        client_pending_orders = Client.objects.filter(pk=value).first()

        if client_pending_orders is None:
            return value

        raise ValidationError('Client might have only one order in time')

    def get_other_pending_orders_of_driver(self, value):
        # Because there is OneToOne link between car and driver, we have a possibility do not checking car avalible :-)
        driver_pending_orders = Driver.objects.filter(pk=value).first()

        if driver_pending_orders is None:
            return value

        raise ValidationError('Driver might have only one order in time')

    def create(self, validated_data):
        client = validated_data.pop('client')
        driver = validated_data.pop('driver')

        return Order.objects.create(**validated_data)




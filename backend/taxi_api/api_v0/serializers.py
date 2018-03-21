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
        fields = ('id', 'name', 'description', 'driver', 'number')
        number = serializers.CharField(max_length=8, required=False, default='AAA 890')
        # fields = '__all__'

    def validate_number(self, value):
        """
        There is two patterns of car number. Check it
        """
        pattern1 = re.compile(r"^[A-Z]{3}\ [0-9]{3}$")
        pattern2 = re.compile(r"^[A-Z]{2}\ [0-9]{3}\ [A-Z]{1}$")

        if pattern1.match(value) or pattern2.match(value):
            return value

        raise ValidationError("Car number should be like AAA 777 or AA 777 A")

    # def create(self, validated_data):
    #     number = validated_data.pop('number', )
    #
    #     return validated_data
    #
    #     # return Car.objects.create(**validated_data)


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ('id', 'name', 'cost_per_km')


class OrderSerializer(serializers.ModelSerializer):

    client = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=Client.objects.get_queryset())
    driver = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=Driver.objects.get_queryset())
    tariff = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=Tariff.objects.get_queryset())
    car = serializers.PrimaryKeyRelatedField(allow_null=False, queryset=Car.objects.get_queryset())

    # This field should be written without user input
    stop_taxiing_time = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = Order

        # Start taxing time describe in model like `auto_now_add`, so exclude it

        fields = ('id', 'client', 'driver', 'tariff', 'car', 'start_taxiing_time', 'stop_taxiing_time')

    def validate_client(self, value):

        # try:
        #     client = Client.objects.get(pk=value)
        # except Client.DoesNotExist:
        #     raise ValidationError("Client doesn't exist")

        try:
            client_pending_orders = Order.objects.get(client_id=value, stop_taxiing_time__isnull=True)
        except:
            client_pending_orders = None

        if client_pending_orders is not None:
            raise ValidationError('Client might have only one order in time')

        return value

    def validate_driver(self, value):

        # try:
        #     driver = Driver.objects.get(pk=value)
        # except Driver.DoesNotExist:
        #     raise ValidationError("Driver doesn't exist")

        # Because there is OneToOne link between car and driver, we have a possibility do not checking car avalible :-)
        try:
            driver_pending_orders = Order.objects.get(driver_id=value, stop_taxiing_time__isnull=True)
        except:
            driver_pending_orders = None

        if driver_pending_orders is not None:
            raise ValidationError('Driver might have only one order in time')

        return value

    def validate_tariff(self, value):
        if value is None:
            raise ValidationError("Tariff doesn't exist")

        else:
            return value

    def validate_car(self, value):
        if value is None:
            raise ValidationError("Car doesn't exist")

        else:
            return value

    # def validate_stop_taxiing_time(self, value):
    #     if self.stop_taxiing_time is not None:
    #         raise ValidationError('Order is finished')
    #
    #     return value

    def create(self, validated_data) -> Driver:
        client = validated_data.pop('client')
        driver = validated_data.pop('driver')
        tariff = validated_data.pop('tariff')
        return Order.objects.create(
            client=client,
            driver=driver,
            tariff=tariff,
            **validated_data,
        )

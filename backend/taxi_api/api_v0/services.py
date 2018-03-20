from django.http import HttpResponse
from rest_framework import status
from api_v0.models import Client, Driver, Car, Tariff, Order
from api_v0.serializers import ClientSerializer, DriverSerializer, CarSerializer, TariffSerializer, OrderSerializer


# Client section


class ClientsService:

    def get_client_list(self):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return serializer.data

    def post_client_list(self, data):
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        return serializer.errors, status.HTTP_400_BAD_REQUEST


class SingleClientService:

    def __init__(self, client: Client):
        self.client = client

    def get_client_detail(self):
        serializer = ClientSerializer(self.client)
        return serializer.data

    def put_client_detail(self, data):
        serializer = ClientSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED

        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_client_detail(self):

        self.client.delete()
        return status.HTTP_204_NO_CONTENT


# Driver section


class DriversService:

    def get_driver_list(self):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return serializer.data

    def post_driver_list(self, data):
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        return serializer.errors, status.HTTP_400_BAD_REQUEST


class SingleDriverService:

    def __init__(self, driver: Driver):
        self.driver = driver

    def get_driver_detail(self):
        serializer = DriverSerializer(self.driver)
        return serializer.data

    def put_driver_detail(self, data):
        serializer = DriverSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED

        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_driver_detail(self):

        self.driver.delete()
        return status.HTTP_204_NO_CONTENT


# Car section


class CarsService:

    def get_car_list(self):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return serializer.data

    def post_car_list(self, data):
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        return serializer.errors, status.HTTP_400_BAD_REQUEST


class SingleCarService:

    def __init__(self, car: Car):
        self.car = car

    def get_car_detail(self):
        serializer = CarSerializer(self.car)
        return serializer.data

    def put_car_detail(self, data):
        serializer = CarSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED

        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_car_detail(self):

        self.car.delete()
        return status.HTTP_204_NO_CONTENT


# Tariff section


class TariffsService:

    def get_tariff_list(self):
        tariffs = Tariff.objects.all()
        serializer = TariffSerializer(tariffs, many=True)
        return serializer.data

    def post_tariff_list(self, data):
        serializer = TariffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        return serializer.errors, status.HTTP_400_BAD_REQUEST


class SingleTariffService:

    def __init__(self, tariff: Tariff):
        self.tariff = tariff

    def get_tariff_detail(self):
        serializer = TariffSerializer(self.tariff)
        return serializer.data

    def put_tariff_detail(self, data):
        serializer = TariffSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED

        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_tariff_detail(self):

        self.tariff.delete()
        return status.HTTP_204_NO_CONTENT


# Order section


class OrdersService:

    def get_order_list(self):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return serializer.data

    def post_order_list(self, data):
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED
        return serializer.errors, status.HTTP_400_BAD_REQUEST


class SingleOrderService:

    def __init__(self, order: Order):
        self.order = order

    def get_order_detail(self):
        serializer = OrderSerializer(self.order)
        return serializer.data

    def put_order_detail(self, data):
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return serializer.data, status.HTTP_201_CREATED

        return serializer.errors, status.HTTP_400_BAD_REQUEST

    def delete_order_detail(self):

        self.order.delete()
        return status.HTTP_204_NO_CONTENT
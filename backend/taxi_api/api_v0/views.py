from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from api_v0.models import Client, Driver, Car, Tariff, Order
from api_v0.serializers import CarSerializer, TariffSerializer, OrderSerializer
from api_v0.services import ClientsService, SingleClientService, DriversService, SingleDriverService, \
    CarsService, SingleCarService, TariffsService, SingleTariffService, OrdersService, SingleOrderService

# Create your views here.


def index(request):
    return HttpResponse('Hello')

# Client section


@api_view(['GET', 'POST'])
def client_list(request, format=None):
    if request.method == 'GET':
        response = ClientsService().get_client_list()
        return Response(response)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        response = ClientsService().post_client_list(data=data)
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk, format=None):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = SingleClientService(client).get_client_detail()
        return Response(response)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        response = SingleClientService(client).put_client_detail(data=data)
        return Response(response)

    elif request.method == 'DELETE':
        response = SingleClientService(client).delete_client_detail()
        return HttpResponse(response)


# Driver section

@api_view(['GET', 'POST'])
def driver_list(request, format=None):
    if request.method == 'GET':
        response = DriversService().get_driver_list()
        return Response(response)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        response = DriversService().post_driver_list(data=data)
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, pk, format=None):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = SingleDriverService(driver).get_driver_detail()
        return Response(response)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        response = SingleDriverService(driver).put_driver_detail(data=data)
        return Response(response)

    elif request.method == 'DELETE':
        response = SingleDriverService(driver).delete_driver_detail()
        return HttpResponse(response)


# Car section

@api_view(['GET', 'POST'])
def car_list(request, format=None):
    if request.method == 'GET':
        response = CarsService().get_car_list()
        return Response(response)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        response = CarsService().post_car_list(data=data)
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk, format=None):
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = SingleCarService(car).get_car_detail()
        return Response(response)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        response = SingleCarService(car).put_car_detail(data=data)
        return Response(response)

    elif request.method == 'DELETE':
        response = SingleCarService(car).delete_car_detail()
        return HttpResponse(response)


# Tariff section

@api_view(['GET', 'POST'])
def tariff_list(request, format=None):
    if request.method == 'GET':
        response = TariffsService().get_tariff_list()
        return Response(response)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        response = TariffsService().post_tariff_list(data=data)
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
def tariff_detail(request, pk, format=None):
    try:
        tariff = Tariff.objects.get(pk=pk)
    except Tariff.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = SingleTariffService(tariff).get_tariff_detail()
        return Response(response)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        response = SingleTariffService(tariff).put_tariff_detail(data=data)
        return Response(response)

    elif request.method == 'DELETE':
        response = SingleTariffService(tariff).delete_tariff_detail()
        return HttpResponse(response)


# Order section

@api_view(['GET', 'POST'])
def order_list(request, format=None):
    if request.method == 'GET':
        response = OrdersService().get_order_list()
        return Response(response)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        response = OrdersService().post_order_list(data=data)
        return Response(response)


@api_view(['GET', 'PUT', 'DELETE'])
def order_detail(request, pk, format=None):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response = SingleOrderService(order).get_order_detail()
        return Response(response)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        response = SingleOrderService(order).put_order_detail(pk=pk)
        return Response(response)

    elif request.method == 'DELETE':
        response = SingleOrderService(order).delete_order_detail()
        return HttpResponse(response)

@api_view(['GET'])
def order_stop(request, pk, format=None):
    try:
        order = Order.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)



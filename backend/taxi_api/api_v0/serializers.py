from rest_framework import serializers
from .models import Client, Driver, Tariff, Car, Order


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')

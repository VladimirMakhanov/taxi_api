from django.http import HttpResponse
from rest_framework import status
from api_v0.models import Client, Order
from api_v0.serializers import ClientSerializer, OrderSerializer


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
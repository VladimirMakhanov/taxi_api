from api_v0.models import Client, Order
from api_v0.serializers import ClientSerializer, OrderSerializer


def create_order(data):
    order = OrderSerializer()
from rest_framework import viewsets
from yume.models import Product, Order, ProductOrder
from yume.serializers import (ProductSerializer, OrderSerializer,
                              ProductOrderSerializer)
from yume.pagination import CustomPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination


class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    pagination_class = CustomPagination

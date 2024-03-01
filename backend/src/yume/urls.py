from django.urls import path, include
from rest_framework import routers
from yume.views import ProductViewSet, OrderViewSet, ProductOrderViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, 'products')
router.register(r'orders', OrderViewSet, 'orders')
router.register(r'product_orders', ProductOrderViewSet, 'product_orders')

urlpatterns = [
    path('', include(router.urls)),
]

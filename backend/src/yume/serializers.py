from rest_framework import serializers
from yume.models import Product, Order, ProductOrder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductOrderSerializer(serializers.ModelSerializer):
    def validate(self, data):
        product = data['product']
        order = data['order']
        rent_start_date = order.start_date
        rent_end_date = order.end_date
        queryset = ProductOrder.objects.filter(
            product=product,
            order__start_date__lte=rent_end_date,
            order__end_date__gte=rent_start_date
        )
        if queryset.exists():
            raise serializers.ValidationError(
                {'product': 'Данный продукт уже зарезервирован на этот период'}
                )
        return super().validate(data)
    
    def create(self, validated_data):
        validated_data["price"] = validated_data["product"].price * (
            validated_data["order"].end_date -
            validated_data["order"].start_date).days
        return super().create(validated_data)

    class Meta:
        model = ProductOrder
        fields = '__all__'
        read_only_fields = ('price',)

from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'product_sku', 'size', 'color', 'quantity', 'price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'shipping_name', 'shipping_email', 'shipping_city', 'shipping_country',
            'subtotal', 'shipping_cost', 'total_price',
            'status', 'payment_status', 'tracking_number', 'tracking_url',
            'items', 'created_at',
        ]
        read_only_fields = ['status', 'payment_status', 'tracking_number', 'total_price']

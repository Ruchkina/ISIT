from shop.models import Performance, Customer, Theatre, Order, OrderTheatre
from rest_framework import serializers

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ["pk", "name", "theatre", "description", "image", "price", "data_perform"]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["pk", "first_name", "last_name", "email"]

class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = ["pk", "director", "description", "address"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pk", "data", "customer_rk"]

class OrderTheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTheatre
        fields = ["pk", "order_rk", "performance_rk"]
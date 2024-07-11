from rest_framework import serializers
from .models import Customer, Order

#Customer serialiser
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = ['id', 'name', 'phone_number']

#Order serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['id', 'customer', 'item', 'amount', 'time']
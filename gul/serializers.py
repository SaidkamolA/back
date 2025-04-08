from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'product', 'quantity', 'phone', 'receipt', 'status', 'created_at']
        read_only_fields = ['created_at']  # Только created_at не может быть изменен
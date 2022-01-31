from RestApp.models import OrderItem

from rest_framework import serializers

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

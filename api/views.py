# from django.shortcuts import render
# Create your views here.

from RestApp.models import OrderItem
from .serializers import OrderItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def PushOIView(request):
    if request.method == 'POST':
        serializer = OrderItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
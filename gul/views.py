from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from .models import Order
from .serializers import OrderSerializer

class IsBotOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        # Allow access if user is authenticated
        if request.user and request.user.is_authenticated:
            return True
        
        # Allow access if request is from the bot (no auth header)
        if not request.headers.get('Authorization'):
            return True
            
        return False

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsBotOrAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status = self.request.query_params.get('status', None)
        
        # If request is from bot, return all orders
        if not self.request.headers.get('Authorization'):
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.filter(user=user)
            
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    def perform_create(self, serializer):
        if self.request.user and self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

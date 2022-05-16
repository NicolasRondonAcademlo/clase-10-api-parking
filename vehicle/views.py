from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from .permissions import IsOwnerOrReadOnlyVehicle
from rest_framework.permissions import  IsAdminUser

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerOrReadOnlyVehicle]
        return [permission() for permission in permission_classes]

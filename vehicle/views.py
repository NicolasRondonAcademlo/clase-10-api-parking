from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Vehicle
from .serializers import VehicleSerializer
from .permissions import IsOwnerOrReadOnlyVehicle
from rest_framework.permissions import  IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    # def get_queryset(self):
    #     queryset = Vehicle.objects.filter(color)
    #     color = self.request.query_params.get('color', None)
    #     if color is not None:
    #         queryset = queryset.filter(color=color)
    #     return queryset
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['color', 'plate']
    search_fields = ['color']

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsOwnerOrReadOnlyVehicle]
        return [permission() for permission in permission_classes]

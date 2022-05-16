from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializers import UserSerializer
from .models import User
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer
from rest_framework.response import Response
from  rest_framework import status
from place.models import RackItem
from place.serializers import RackSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset =  User.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    @action(detail=True)
    def my_cars(self, request,  pk=None):
        queryset = Vehicle.objects.filter(
            owner__id=pk
        )
        serializer = VehicleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    @action(detail=True)
    def my_cars_on_parking(self, request,  pk=None):
        queryset = RackItem.objects.filter(
            vehicle__owner__id=pk
        ).values_list("vehicle__id", flat=True)
        vehicles = Vehicle.objects.filter(
            id__in=queryset
        )
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
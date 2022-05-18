from django.shortcuts import render
from rest_framework import viewsets
from .models import RackItem, Rack
from .serializers import RackItemSerializer, RackSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrReadOnlyVehicle



# Create your views here.
class RackItemViewSet(viewsets.ModelViewSet):
    queryset = RackItem.objects.all()
    serializer_class = RackItemSerializer
    permission_classes = [IsAdminUser, IsOwnerOrReadOnlyVehicle]



class RackViewSet(viewsets.ModelViewSet):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer

    @action(detail=False)
    def available_racks(self, request):
        racks = Rack.objects.filter(status=True)
        serializer = RackSerializer(racks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(detail=False)
    def busy_racks(self, request):
        racks = Rack.objects.filter(status=False)
        serializer = RackSerializer(racks, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

from rest_framework import serializers
from .models import Vehicle
from core.serializers import UserSerializer


class VehicleSerializer(serializers.ModelSerializer):
    vehicle = serializers.CharField(source='get_vehicle_display')
    class Meta:
        model = Vehicle
        fields = "__all__"


class VehicleUserSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Vehicle
        fields = "__all__"

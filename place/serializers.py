from rest_framework import serializers
from .models import RackItem, Rack
from vehicle.serializers import VehicleUserSerializer


class RackItemSerializer(serializers.ModelSerializer):
    vehicle = VehicleUserSerializer()
    class Meta:
        model = RackItem
        fields = "__all__"
        depth = 1


class RackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rack
        fields = "__all__"
        depth = 1
from django.db import models
from core.models import User
# Create your models here.

class Vehicle(models.Model):

    VEHICLES_CHOICES = [
        ("c", "Car" ),
        ("m", "Motorbike"),
        ("b", "Bike")
    ]
    ENGINE_CHOICES = [
        ("c", "combustion"),
        ("e", "electric")
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.CharField(choices=VEHICLES_CHOICES, max_length=1)
    plate = models.CharField(max_length=6)
    color = models.CharField(max_length=25)
    engine = models.CharField(choices=ENGINE_CHOICES, max_length=1, blank=True, null=True)

    def __str__(self):
        return f"{self.plate} | {self.vehicle} | {self.owner.email}"
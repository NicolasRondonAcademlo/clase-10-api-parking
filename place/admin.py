from django.contrib import admin
from .models import Place, Rack, RackItem
# Register your models here.

admin.site.register(Place)
admin.site.register(Rack)
admin.site.register(RackItem)
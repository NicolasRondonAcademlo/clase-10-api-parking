from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet

router = DefaultRouter()
router.register("vehicle", VehicleViewSet)

urlpatterns = router.urls
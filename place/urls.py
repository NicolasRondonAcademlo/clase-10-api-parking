from rest_framework.routers import DefaultRouter
from .views import RackItemViewSet, RackViewSet
router = DefaultRouter()
router.register("rack_item", RackItemViewSet)
router.register("racks", RackViewSet)
urlpatterns = router.urls
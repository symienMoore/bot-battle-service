from rest_framework import routers
from .api import RobotViewSet
from .models import Robot

router = routers.DefaultRouter()
router.register('/api/robot', RobotViewSet, 'Robot')

urlpatterns = router.urls
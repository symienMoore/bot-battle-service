from Bot.models import Robot
from rest_framework import viewsets, permissions
from .serializers import RobotSerializer

class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = RobotSerializer
from rest_framework import serializers
from Bot.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'
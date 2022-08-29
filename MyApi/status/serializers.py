from rest_framework import serializers
from .models import StatusModel


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = ['id', 'user', 'content', 'image']

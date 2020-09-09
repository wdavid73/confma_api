from rest_framework import serializers

from ..Domain.ModelShirtsUniformSports import ShirtsUniformSports


class ShirtsSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsUniformSports
        fields = ['id', 'size', 'type', 'image']

from rest_framework import serializers

from ..Domain.ModelShirtsSports import ShirtsSports


class ShirtsSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsSports
        fields = ['id', 'size', 'image','price']

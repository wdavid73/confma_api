from rest_framework import serializers

from ..Domain.ModelSweatShirtUniformSports import SweatShirtUniformSports


class SweatShirtSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SweatShirtUniformSports
        fields = ['id', 'size', 'image']

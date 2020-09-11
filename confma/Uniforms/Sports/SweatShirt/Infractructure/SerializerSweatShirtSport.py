from rest_framework import serializers

from ..Domain.ModelSweatShirt import SweatShirt


class SweatShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = SweatShirt
        fields = ['id', 'size', 'image']

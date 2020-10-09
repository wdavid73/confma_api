from rest_framework import serializers

from ..Domain.ModelDresses import DressesUniform


class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DressesUniform
        fields = ['id', 'ref', 'size', 'price', 'image']

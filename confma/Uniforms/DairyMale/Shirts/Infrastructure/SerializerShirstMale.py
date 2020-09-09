from rest_framework import serializers

from ..Domain.ModelShirtsUniformMale import ShirtsUniformMale


class ShirtsMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsUniformMale
        fields = ['id', 'size', 'image']

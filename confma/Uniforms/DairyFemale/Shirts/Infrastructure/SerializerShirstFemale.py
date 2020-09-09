from rest_framework import serializers

from ..Domain.ModelShirtsUniformFemale import ShirtsUniformFemale


class ShirstFemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsUniformFemale
        fields = ['id', 'size', 'image']

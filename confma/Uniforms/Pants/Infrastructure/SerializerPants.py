from rest_framework import serializers

from ..Domain.ModelPants import Pants


class PantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pants
        fields = ['id', 'ref', 'size', 'price', 'type', 'image']

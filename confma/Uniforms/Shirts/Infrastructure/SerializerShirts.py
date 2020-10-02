from rest_framework import serializers

from ..Domain.ModelShirts import Shirts


class ShirtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirts
        fields = ['id',  'ref', 'size', 'price', 'type', 'image']

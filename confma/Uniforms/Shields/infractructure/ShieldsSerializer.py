from rest_framework import serializers

from ..domain.ModelShields import Shields


class ShieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shields
        fields = ['id', 'name_college', 'price', 'image']

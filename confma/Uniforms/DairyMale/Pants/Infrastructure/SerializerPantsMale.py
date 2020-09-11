from rest_framework import serializers

from ..Domain.ModelPantsMale import PantsMale


class PantsMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantsMale
        fields = ['id', 'size','price', 'image']

from rest_framework import serializers

from ..Domain.ModelPantsUniformMale import PantsUniformMale


class PantsMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PantsUniformMale
        fields = ['id', 'size', 'image']

from rest_framework import serializers

from ..Domain.ModelShirtsMale import ShirtsMale


class ShirtsMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsMale
        fields = ['id', 'size', 'image']

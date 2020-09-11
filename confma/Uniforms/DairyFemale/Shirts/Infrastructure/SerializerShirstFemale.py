from rest_framework import serializers

from ..Domain.ModelShirtsFemale import ShirtsFemale


class ShirtsFemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsFemale
        fields = ['id', 'size', 'price','image']

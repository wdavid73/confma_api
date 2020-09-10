from rest_framework import serializers

from ..Domain.ModelShirtsFemale import ShirtsFemale


class ShirstFemaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShirtsFemale
        fields = ['id', 'size', 'image']

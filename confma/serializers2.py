from rest_framework import serializers

from .models import QuotationClient


class QuotationClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuotationClient
        fields = ['url', 'id', 'quotation', 'client', 'total']

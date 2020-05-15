from rest_framework import serializers

from ...Clients.Infrastructure.SerializerClient import ClientSerializer
from ..Infrastructure.SerializerQuotation import QuotationSerializer
from ..Domain.ModelQuotation import QuotationClient, Client, Quotation


class QuotationClientSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True, many=False)
    clientId = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Client.objects.filter(state=1),
        source='client'
    )
    quotation = QuotationSerializer(read_only=True, many=False)
    quotationId = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Quotation.objects.filter(state=1),
        source="quotation"
    )

    class Meta:
        model = QuotationClient
        fields = ['id', 'quotation', 'quotationId', 'client', 'clientId']
        extra_kwargs = {
            "quotation": {
                "error_messages":
                    {
                        "required": "Please Select a Quotation for Save",
                    }
            },
            "client": {
                "error_messages":
                    {
                        "required": "Please Select a Client for Save",
                    }
            },
            "total": {
                "error_messages":
                    {
                        "required": "Please Enter a Total of Quotation",
                    }
            }
        }

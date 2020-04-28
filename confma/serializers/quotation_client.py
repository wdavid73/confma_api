from rest_framework import serializers

from .client import ClientSerializer
from .links import quotation_client_link
from .quotation import QuotationSerializer
from ..models import QuotationClient,Client


class QuotationClientSerializer(serializers.ModelSerializer):
    url = quotation_client_link
    client = ClientSerializer(read_only=True, many=False)
    clientId = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset = Client.objects.filter(state=1),
        source='client'
    )
    quotation = QuotationSerializer(read_only=True, many=False)

    class Meta:
        model = QuotationClient
        fields = ['url', 'id', 'quotation', 'client','clientId' ,'total']
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

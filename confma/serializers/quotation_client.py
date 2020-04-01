from rest_framework import serializers

from .client import ClientSerializer
from .links import quotation_client_link
from .quotation import QuotationSerializer
from ..models import QuotationClient


class QuotationClientSerializer(serializers.ModelSerializer):
    url = quotation_client_link
    client = ClientSerializer(read_only=True, many=False)
    quotation = QuotationSerializer(read_only=True, many=False)

    class Meta:
        model = QuotationClient
        fields = ['url', 'id', 'quotation', 'client', 'total']
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

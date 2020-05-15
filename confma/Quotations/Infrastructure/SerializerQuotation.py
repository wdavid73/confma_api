from rest_framework import serializers

from ...Cloths.Infrastruture.SerializerCloth import ClothSerializer
from ..Domain.ModelQuotation import Quotation
from ...Cloths.Domain.ModelCloth import Cloth


class QuotationSerializer(serializers.ModelSerializer):
    cloth = ClothSerializer(read_only=True)
    clothId = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Cloth.objects.filter(state=1),
        source='cloth'
    )

    class Meta:
        model = Quotation
        fields = ['id', 'value_cloth',
                  'value_work', 'value_threads', 'value_buttons',
                  'value_necks', 'value_embroidery', 'value_prints',
                  'cloth', 'clothId', 'total']
        extra_kwargs = {
            "value_cloth": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Cloth",
                        "invalid": "Please Enter a Value Valid"
                    }
            },
            "value_work": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Work",

                        "invalid": "Please Enter a Value Valid",
                    }
            },
            "value_threads": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Threads",

                        "invalid": "Please Enter a Value Valid",
                    }
            },
            "value_buttons": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Buttons",

                        "invalid": "Please Enter a Value Valid",
                    }
            },
            "value_necks": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Necks",

                        "invalid": "Please Enter a Value Valid",
                    }
            },
            "value_embroidery": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Embroidery",

                        "invalid": "Please Enter a Value Valid",
                    }
            },
            "value_prints": {
                "error_messages":
                    {
                        "required": "Please enter the Value of Prints",

                        "invalid": "Please Enter a Value Valid",
                    }
            },
            "cloth": {
                "error_messages":
                    {
                        "required": "Please Select a Cloth for the Quotation",
                    }
            },

        }

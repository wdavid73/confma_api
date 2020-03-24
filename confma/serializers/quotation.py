from rest_framework import serializers

from ..models import Quotation


class QuotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quotation

        fields = ['url', 'id', 'value_cloth',
                  'value_work', 'value_threads', 'value_buttons',
                  'value_necks', 'value_embroidery', 'value_prints',
                  'cloth', 'client']

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
            "client": {
                "error_messages":
                    {
                        "required": "Please Select a Client for the Quotation",
                    }
            },

        }

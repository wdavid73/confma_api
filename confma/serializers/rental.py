from rest_framework import serializers

from .client import ClientSerializer
from .cloth import ClothSerializer
from .links import rental_link
from ..models import Rental


class RentalSerializer(serializers.ModelSerializer):
    url = rental_link
    client = ClientSerializer(read_only=True, many=False)
    cloth = ClothSerializer(read_only=True, many=False)

    class Meta:
        model = Rental
        fields = ['url', 'id', 'date_return', 'price', 'cloth', 'client']
        extra_kwargs = {
            "price": {
                "error_messages":
                    {
                        "required": "Please enter a Price for the Rental",
                        "invalid": "Please Enter a Price Valid"
                    }
            },
            "cloth": {
                "error_messages":
                    {
                        "required": "Please Select a Cloth for the Rental",
                    }
            },
            "client": {
                "error_messages":
                    {
                        "required": "Please Select a Client for the Rental",
                    }
            },
            "date_return": {
                "error_messages":
                    {
                        "required": "please enter a date of return the Rental",
                        "invalid": "Please Enter a Date Valid"
                    }
            }
        }

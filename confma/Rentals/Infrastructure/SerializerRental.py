from rest_framework import serializers

from ...Clients.Domain.ModelClient import Client
from ...Clients.Infrastructure.SerializerClient import ClientSerializer
from ...Cloths.Domain.ModelCloth import Cloth
from ...Cloths.Infrastruture.SerializerCloth import ClothSerializer
from ...Rentals.Domain.ModelRental import Rental


class RentalSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    clientId = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Client.objects.filter(state=1),
        source='client'
    )
    cloth = ClothSerializer(read_only=True)
    clothId = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Cloth.objects.filter(state=1),
        source='cloth'
    )

    class Meta:
        model = Rental
        fields = ['id', 'date_return', 'price', 'ifrental',
                  'cloth', 'clothId', 'client', 'clientId', ]
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

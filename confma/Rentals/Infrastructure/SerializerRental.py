from rest_framework import serializers

from ...Clients.Domain.ModelClient import Client
from ...Clients.Infractructure.SerializerClient import ClientSerializer
from ...Cloths.Domain.ModelCloth import Cloth
from ...Cloths.Infrastruture.SerializerCloth import ClothSerializer
from ...Rentals.Domain.ModelRental import Rental


class RentalSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Client.objects.filter(state=1),
        source='client'
    )
    cloth = ClothSerializer(read_only=True)
    cloth_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Cloth.objects.filter(state=1),
        source='cloth'
    )

    class Meta:
        model = Rental
        fields = ['id', 'date_return', 'date_now', 'price', 'ifrental',
                  'cloth', 'cloth_id', 'client', 'client_id', ]
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

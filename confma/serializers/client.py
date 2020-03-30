from rest_framework import serializers

from .links import client_link
from ..models import Client


class ClientSerializer(serializers.ModelSerializer):
    url = client_link

    class Meta:
        model = Client
        fields = ['url', 'id', 'name', 'last_name', 'address', 'phone', 'cellphone']
        extra_kwargs = {
            "name": {
                "error_messages":
                    {
                        "required": "Please enter your Name",
                        "invalid": "Please Enter a Name Valid"
                    }
            },
            "last_name": {
                "error_messages":
                    {
                        "required": "Please enter your Last Name",
                        "invalid": "Please Enter a Last Name Valid"
                    }
            },
            "address": {
                "error_messages":
                    {
                        "required": "Please enter your Address",
                        "invalid": "Please Enter a Address Valid"
                    }
            },
            "phone": {
                "error_messages":
                    {
                        "required": "Please enter a Phone Number",
                        "invalid": "Please Enter a Phone Number Valid"
                    }
            },
            "cellphone": {
                "error_messages":
                    {
                        "required": "Please enter a Cellphone Number",
                        "invalid": "Please Enter a Cellphone Number Valid"
                    }
            }
        }

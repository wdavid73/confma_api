from rest_framework import serializers

from ..Domain.ModelDresses import DressesUniform


class DressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DressesUniform
        fields = ['id', 'ref', 'size', 'price', 'image']
        extra_kwargs = {
            "ref": {
                "error_messages":
                    {
                        "required": "Please enter your Name",
                        "invalid": "Please Enter a Name Valid",
                        "blank": "Porfavor este campo no puede estar vacio"
                    }
            }
        }

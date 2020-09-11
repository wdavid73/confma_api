from rest_framework import serializers

from ..Domain.ModelUniformSports import UniformsSports


class UniformSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniformsSports
        fields = ['id', 'name_college', 'price', 'type_uniform']

        extra_kwargs = {
            "name_college": {
                "error_messages":
                    {
                        "required": "please enter a name of college",
                        "invalid": "please enter a valid name"
                    }
            },
            "price": {
                "error_messages":
                    {
                        "required": "please enter a price of uniform",
                        "invalid": "please enter a valid price"
                    }
            },
            "type_uniform": {
                "error_messages":
                    {
                        "required": "please select a type of uniform of uniform",
                        "invalid": "please select a valid type of uniform"
                    }
            },
        }

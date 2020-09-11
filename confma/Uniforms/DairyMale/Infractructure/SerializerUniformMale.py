from rest_framework import serializers

from ..Domain.ModelUniformMale import UniformsMale
from ..Shirts.Domain.ModelShirtsMale import ShirtsMale
from ..Pants.Domain.ModelPantsMale import PantsMale
from ..Shirts.Infrastructure.SerializerShirstMale import ShirtsMaleSerializer
from ..Pants.Infrastructure.SerializerPantsMale import PantsMaleSerializer

class UniformMaleSerializer(serializers.ModelSerializer):
    pants = PantsMaleSerializer(read_only = True)
    pants_id = serializers.PrimaryKeyRelatedField(
        write_only = True,
        queryset=PantsMale.objects.filter(state=1),
        source="pants"
    )

    shirt = ShirtsMaleSerializer(read_only=True)
    shirt_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=ShirtsMale.objects.filter(state=1),
        source='shirt'
    )

    class Meta:
        model = UniformsMale
        fields = ['id', 'name_college''price','pants_id','pants','shirt_id','shirt']

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
                        "required": "please input a price of uniform",
                        "invalid": "please input a valid price"
                    }
            },

            "pants_id": {
                "error_messages":
                    {
                        "required": "please input a pants",
                        "invalid": "please input a valid pants"
                    }
            },

            "shirt_id": {
                "error_messages":
                    {
                        "required": "please input a shirt ",
                        "invalid": "please input a valid shirt"
                    }
            }
        }

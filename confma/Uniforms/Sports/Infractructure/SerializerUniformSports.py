from rest_framework import serializers

from ..Domain.ModelUniformSports import UniformsSports
from ...Shirts.Domain.ModelShirts import Shirts
from ...Shirts.Infrastructure.SerializerShirts import ShirtsSerializer
from ...Pants.Infrastructure.SerializerPants import PantsSerializer
from ...Pants.Domain.ModelPants import Pants


class UniformSportsSerializer(serializers.ModelSerializer):
    shirt = ShirtsSerializer(read_only=True)
    shirt_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Shirts.objects.filter(state=1),
        source="shirt"
    )

    pants = PantsSerializer(read_only=True)
    pants_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Pants.objects.filter(state=1),
        source="pants"
    )

    class Meta:
        model = UniformsSports
        fields = ['id', 'name_college', 'shirt',
                  'shirt_id', 'pants', 'pants_id']

        extra_kwargs = {
            "name_college": {
                "error_messages":
                    {
                        "required": "please enter a name of college",
                        "invalid": "please enter a valid name"
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

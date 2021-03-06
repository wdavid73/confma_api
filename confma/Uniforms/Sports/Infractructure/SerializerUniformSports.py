from rest_framework import serializers

from ..Domain.ModelUniformSports import UniformsSports
from ...Shirts.Domain.ModelShirts import Shirts
from ...Pants.Domain.ModelPants import Pants
from ....Institution.Domain.Institution import Institution
from ...Shirts.Infrastructure.SerializerShirts import ShirtsSerializer
from ...Pants.Infrastructure.SerializerPants import PantsSerializer
from ....Institution.Infractructure.SerializerInstitution import SerializerInstitution


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

    institution = SerializerInstitution(read_only=True)
    institution_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Institution.objects.filter(state=1),
        source="institution"
    )

    class Meta:
        model = UniformsSports
        fields = ['id', "price", "type_uniform", 'institution_id', 'institution', 'shirt',
                  'shirt_id', 'pants', 'pants_id']

        extra_kwargs = {
            "type_uniform": {
                "error_messages":
                    {
                        "required": "please select a type of uniform of uniform",
                        "invalid": "please select a valid type of uniform"
                    }
            },
        }

from rest_framework import serializers

from ..Domain.ModelUniformMale import UniformsMale
from ...Shirts.Domain.ModelShirts import Shirts
from ...Pants.Domain.ModelPants import Pants
from ....Institution.Domain.Institution import Institution
from ...Shirts.Infrastructure.SerializerShirts import ShirtsSerializer
from ...Pants.Infrastructure.SerializerPants import PantsSerializer
from ....Institution.Infractructure.SerializerInstitution import SerializerInstitution


class UniformMaleSerializer(serializers.ModelSerializer):
    pants = PantsSerializer(read_only=True)
    pants_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Pants.objects.filter(state=1, type="Male"),
        source="pants"
    )

    institution = SerializerInstitution(read_only=True)
    institution_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Institution.objects.filter(state=1),
        source="institution"
    )

    shirt = ShirtsSerializer(read_only=True)
    shirt_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Shirts.objects.filter(state=1, type="Male"),
        source='shirt'
    )

    class Meta:
        model = UniformsMale
        fields = ['id', 'price', 'institution_id', 'institution',
                  'pants_id', 'pants', 'shirt_id', 'shirt']

        extra_kwargs = {
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

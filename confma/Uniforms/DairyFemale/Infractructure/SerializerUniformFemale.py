from rest_framework import serializers

from ..Domain.ModelUniformFemale import UniformsFemale
from ...Dresses.Infrastructure.SerializerDresses import DressSerializer
from ...Dresses.Domain.ModelDresses import DressesUniform
from ...Shirts.Infrastructure.SerializerShirts import ShirtsSerializer
from ...Shirts.Domain.ModelShirts import Shirts
from ....Institution.Domain.Institution import Institution
from ....Institution.Infractructure.SerializerInstitution import SerializerInstitution
from ...Pants.Domain.ModelPants import Pants
from ...Pants.Infrastructure.SerializerPants import PantsSerializer


class UniformFemaleSerializer(serializers.ModelSerializer):
    dress = DressSerializer(read_only=True)
    dress_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=DressesUniform.objects.filter(state=1),
        source='dress',
        allow_null=True
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
        queryset=Shirts.objects.filter(state=1, type="Female"),
        source='shirt'
    )

    class Meta:
        model = UniformsFemale
        fields = ['id', 'institution', 'institution_id', 'price', 'dress_id',
                  'dress', 'shirt_id', 'shirt']

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

            "dress_id": {
                "error_messages":
                    {
                        "required": "please input a dress",
                        "invalid": "please input a valid dress"
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

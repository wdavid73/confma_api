from rest_framework import serializers

from ..Domain.ModelUniformFemale import UniformsFemale
from ..Dresses.Infrastructure.SerializerDresses import DressSerializer
from ..Dresses.Domain.ModelDresses import DressesUniform
from ..Shirts.Infrastructure.SerializerShirstFemale import ShirstFemaleSerializer
from ..Shirts.Domain.ModelShirtsFemale import ShirtsFemale


class UniformFemaleSerializer(serializers.ModelSerializer):
    dress = DressSerializer(read_only=True)
    dress_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=DressesUniform.objects.filter(state=1),
        source='dress'
    )

    shirt = ShirstFemaleSerializer(read_only=True)
    shirt_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=ShirtsFemale.objects.filter(state=1),
        source='shirt'
    )

    class Meta:
        model = UniformsFemale
        fields = ['id', 'name_college', 'price', 'dress_id',
                  'dress', 'shirt_id', 'shirt']

        extra_kwargs = {
            "name_college": {
                "error_messages":
                    {
                        "required": "please enter a name of college",
                        "invalid": "please enter a valid name"
                    }
            },
            "size": {
                "error_messages":
                    {
                        "required": "please select a size of uniform",
                        "invalid": "please select a valid size"
                    }
            },
            "type_uniform": {
                "error_messages":
                    {
                        "required": "please select a type of uniform of uniform",
                        "invalid": "please select a valid type of uniform"
                    }
            },
            "image": {
                "error_messages":
                    {
                        "required": "please enter a reference image for uniform",
                        "invalid": "Please Enter a image valid"
                    }
            }
        }

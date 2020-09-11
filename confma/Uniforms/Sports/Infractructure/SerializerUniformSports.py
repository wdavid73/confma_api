from rest_framework import serializers

from ..Domain.ModelUniformSports import UniformsSports
from ..SweatShirt.Domain.ModelSweatShirt import SweatShirt
from ..Shirts.Domain.ModelShirtsSports import ShirtsSports
from ..SweatShirt.Infractructure.SerializerSweatShirtSport import SweatShirtSerializer
from ..Shirts.Infractructure.SerializerShirstSport import ShirtsSportsSerializer

class UniformSportsSerializer(serializers.ModelSerializer):
    shirt = ShirtsSportsSerializer(read_only = True)
    shirt_id = serializers.PrimaryKeyRelatedField(
            write_only = True,
            queryset=ShirtsSports.objects.filter(state=1),
            source="shirt"
        )

    sweat_shirt = SweatShirtSerializer(read_only = True)
    sweat_shirt_id = serializers.PrimaryKeyRelatedField(
            write_only = True,
            queryset=SweatShirt.objects.filter(state=1),
            source="sweat_shirt"
        )

    class Meta:
        model = UniformsSports
        fields = ['id', 'name_college','type_uniform','shirt','shirt_id','sweat_shirt','sweat_shirt_id']

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

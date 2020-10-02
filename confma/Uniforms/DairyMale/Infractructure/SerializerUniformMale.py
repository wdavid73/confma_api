from rest_framework import serializers

from ..Domain.ModelUniformMale import UniformsMale
from ...Shirts.Domain.ModelShirts import Shirts
from ...Pants.Domain.ModelPants import Pants
from ...Shirts.Infrastructure.SerializerShirts import ShirtsSerializer
from ...Pants.Infrastructure.SerializerPants import PantsSerializer

class UniformMaleSerializer(serializers.ModelSerializer):
    pants = PantsSerializer(read_only = True)
    pants_id = serializers.PrimaryKeyRelatedField(
        write_only = True,
        queryset=Pants.objects.filter(state=1,type="Classic Male"),
        source="pants"
    )

    shirt = ShirtsSerializer(read_only=True)
    shirt_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Shirts.objects.filter(state=1,type="Classic Male"),
        source='shirt'
    )

    class Meta:
        model = UniformsMale
        fields = ['id', 'name_college','price','pants_id','pants','shirt_id','shirt']

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

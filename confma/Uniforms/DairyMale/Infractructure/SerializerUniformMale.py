from rest_framework import serializers

from ..Domain.ModelUniformMale import UniformsMale


class UniformMaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniformsMale
        fields = ['id', 'name_college''price']

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
                        "required": "please input a price of uniform",
                        "invalid": "please input a valid price"
                    }
            }
        }

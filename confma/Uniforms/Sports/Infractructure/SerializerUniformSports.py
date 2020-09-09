from rest_framework import serializers

from ..Domain.ModelUniformSports import UniformsSports


class UniformSportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniformsSports
        fields = ['id', 'name_college', 'size', 'type_uniform', 'image']

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

from rest_framework import serializers

from ..models import Cloth


class ClothSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cloth
        fields = ['url', 'id', 'name', 'color', 'size', 'fashion', 'image']
        extra_kwargs = {
            "name": {
                "error_messages":
                    {
                        "required": "please enter a name by which to identify the clothes",
                        "invalid": "Please Enter a Name Valid"
                    }
            },
            "color": {
                "error_messages":
                    {
                        "required": "Please enter a Color in Text",
                        "invalid": "Please Enter a Color Valid"
                    }
            },
            "size": {
                "error_messages":
                    {
                        "required": "Please enter size of cloth",
                        "invalid": "Please Enter a size Valid"
                    }
            },
            "fashion": {
                "error_messages":
                    {
                        "required": "Please enter the Fashion of cloth",
                        "invalid": "Please Enter a Fashion Valid"
                    }
            },
            "image": {
                "error_messages":
                    {
                        "required": "please enter a reference image for clothing",
                        "invalid": "Please Enter a image valid"
                    }
            }
        }

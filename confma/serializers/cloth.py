from rest_framework import serializers

from confecciones_maribel_api.confma.models import Cloth


class ClothSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cloth
        fields = ['url', 'id', 'name', 'color', 'size', 'fashion', 'image']

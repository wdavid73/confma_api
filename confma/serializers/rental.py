from rest_framework import serializers

from confecciones_maribel_api.confma.models import Rental


class RentalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rental
        fields = ['url', 'id', 'date_return', 'price', 'cloth', 'client']

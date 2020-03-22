from rest_framework import serializers

from confecciones_maribel_api.confma.models import Quotation


class QuotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quotation
        fields = ['url',
                  'id',
                  'value_cloth',
                  'value_work',
                  'value_threads',
                  'value_buttons',
                  'value_necks',
                  'value_embroidery',
                  'value_prints',
                  'cloth',
                  'client']

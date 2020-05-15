from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..Domain.ModelQuotation import Quotation
from ...Cloths.Domain.ModelCloth import Cloth
from ...Cloths.Infrastruture.SerializerCloth import ClothSerializer


@api_view(['GET'])
def ClothWithOutQuotation(request):
    quotations = Quotation.objects.filter(
        state=1).values_list('cloth', flat=True)
    cloth_quotation = Cloth.objects.exclude(id__in=quotations)
    response = [ClothSerializer(
        c, context={'request': request}).data for c in cloth_quotation]
    return Response({'response': response}, status=status.HTTP_200_OK)



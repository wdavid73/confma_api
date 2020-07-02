from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelQuotation import Quotation
from ...Cloths.Domain.ModelCloth import Cloth
from ...Cloths.Infrastruture.SerializerCloth import ClothSerializer


@api_view(['GET'])
def ClothWithOutQuotation(request: Request) -> Response:
    quotations = Quotation.objects.filter(state=1).values_list('cloth', flat=True)
    cloth_quotation = Cloth.objects.exclude(id__in=quotations)
    response = [
        ClothSerializer(
            cloth, context={'request': request}
        ).data for cloth in cloth_quotation
    ]
    return Response({'response': response}, status=status.HTTP_200_OK)

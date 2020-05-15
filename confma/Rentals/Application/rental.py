from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Domain.ModelRental import Rental
from ...Cloths.Domain.ModelCloth import Cloth
from ...Cloths.Infrastruture.SerializerCloth import ClothSerializer


@api_view(['GET'])
def ClothWithOutRental(request):
    cloth_with_rental = Rental.objects.filter(state=1, ifrental=1)
    cloths_id = [cr.cloth.id for cr in cloth_with_rental]
    cloth = Cloth.objects.exclude(id__in=cloths_id)
    response = [ClothSerializer(c, context={'request': request}).data
                for c in cloth]
    return Response({'response': response}, status=status.HTTP_200_OK)

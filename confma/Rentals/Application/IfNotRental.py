from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelRental import Rental
from ..Infrastructure.SerializerRental import RentalSerializer


@api_view(['GET'])
def IfNotRental(request: Request) -> Response:
    rental = Rental.objects.filter(ifrental=0)
    serializer = RentalSerializer(rental, many=True,
                                  context={'request': request})
    return Response({'rental': serializer.data},
                    status=status.HTTP_200_OK)

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..Domain.ModelRental import Rental


@api_view(['POST'])
def RefundRental(request, _id):
    if request.method == 'POST':
        rental = get_object_or_404(Rental, id=_id)
        rental.ifrental = 0
        rental.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

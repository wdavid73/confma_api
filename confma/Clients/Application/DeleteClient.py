from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelClient import Client
from ...General.Application.delete import delete
from ...Rentals.Domain.ModelRental import Rental
from ...Quotations.Domain.ModelQuotation import Quotation


@api_view(['POST'])
def delete_log(request: Request, _id: int) -> Response:
    if request.method == 'POST':
        client = get_object_or_404(Client, id=_id)
        rental = Rental.objects.filter(state=1, client=client)
        quotation = Quotation.objects.filter(state=1, client=client)
        if len(rental) == 0 and len(quotation) == 0:
            client.state = 0
            client.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "You Cant Delete the client , because he has rental and quotation actives"},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(
        {"message": "Data invalid"},
        status=status.HTTP_400_BAD_REQUEST
    )

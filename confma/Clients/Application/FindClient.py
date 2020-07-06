from typing import List
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ..Domain.ModelClient import Client
from ..Infrastructure.SerializerClient import ClientSerializer


class FindClient(APIView):
    def get(self, request: Request, id: int) -> Response:
        client = get_object_or_404(Client, id=id)
        quotations = GetQuotationByClient(client, request)
        rentals = GetRentalByClient(client, request)
        serializer = ClientSerializer(client, context={"request": request})
        return Response(
            {"client": serializer.data,
             "quotation": quotations,
             "rental": rentals},
            status=status.HTTP_200_OK)


def GetQuotationByClient(client: Client, request: Request) -> List:
    from ...Quotations.Domain.ModelQuotation import Quotation
    from ...Quotations.Domain.ModelQuotation import QuotationClient
    from ...Quotations.Infrastructure.SerializerQuotation import \
        QuotationSerializer
    quotation_client = QuotationClient.objects.filter(state=1, client=client)
    list_id_qc = [qc.quotation.id for qc in list(quotation_client)]
    response = [
        QuotationSerializer(
            quotation,
            context={"request": request}
        ).data for quotation in Quotation.objects.filter(id__in=list_id_qc)
    ]
    return response


def GetRentalByClient(client: Client, request: Request) -> List:
    from ...Rentals.Domain.ModelRental import Rental
    from ...Rentals.Infrastructure.SerializerRental import RentalSerializer
    response = [
        RentalSerializer(
            rental,
            context={"request": request}
        ).data for rental in Rental.objects.filter(state=1, ifrental=1, client=client)
    ]
    return response

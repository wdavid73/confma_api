from typing import List, Tuple
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ..Domain.ModelClient import Client
from ..Infractructure.SerializerClient import ClientSerializer


class FindClient(APIView):
    def get(self, request: Request, id: int) -> Response:
        client = get_object_or_404(Client, id=id)
        quotations = GetQuotationByClient(client, request)
        rentals, totalQuotation = GetRentalByClient(client, request)
        serializer = ClientSerializer(client,
                                      context={"request": request})
        return Response(
            {"client": serializer.data,
             "quotation": quotations,
             "rental": rentals,
             "totalQuotations": totalQuotation},
            status=status.HTTP_200_OK)


def GetQuotationByClient(client: Client, request: Request) -> List:
    from ...Quotations.Domain.ModelQuotation import Quotation
    from ...Quotations.Domain.ModelQuotation import QuotationClient
    from ...Quotations.Infractructure.SerializerQuotation import \
        QuotationSerializer
    quotation_client = QuotationClient.objects.filter(state=1,
                                                      client=client)
    list_id_qc = [qc.quotation.id for qc in list(quotation_client)]
    response = [
        QuotationSerializer(
            quotation,
            context={"request": request}
        ).data for quotation in
        Quotation.objects.filter(id__in=list_id_qc)
    ]
    return response


def GetRentalByClient(client: Client, request: Request) -> Tuple[
    list, list]:
    from ...Rentals.Domain.ModelRental import Rental
    from ...Cloths.Domain.ModelCloth import Cloth
    from ...Quotations.Domain.ModelQuotation import Quotation
    from ...Rentals.Infrastructure.SerializerRental import \
        RentalSerializer
    from ...Quotations.Infractructure.SerializerQuotation import \
        QuotationSerializer

    rentalsResponse = [
        RentalSerializer(
            rental, context={"request": request}
        ).data for rental in Rental.objects.filter(
            state=1, ifrental=1, client=client)
    ]

    rental = Rental.objects.filter(state=1, ifrental=1,
                                   client=client).values_list("cloth")
    cloth = Cloth.objects.filter(id__in=rental)
    quotationResponse = [
        QuotationSerializer(
            quotation, context={"request": request}
        ).data for quotation in
        Quotation.objects.filter(cloth__in=list(cloth))
    ]
    return rentalsResponse, quotationResponse

from typing import List
from rest_framework.request import Request
from ..Domain.ModelClient import Client
from ...Quotations.Domain.ModelQuotation import QuotationClient
from ...Rentals.Domain.ModelRental import Rental
from ...Rentals.Infrastructure.SerializerRental import RentalSerializer
from ...Quotations.Infrastructure.SerializerQuotationClient import \
    QuotationClientSerializer


def getRentalClient(client: Client, request: Request) -> List:
    response = [
        RentalSerializer(rental, context={'request': request}).data for
        rental in
        Rental.objects.all().filter(state=1, client=client)]
    return response


def getQuotationClient(client: Client, request: Request) -> List:
    quotation_client = QuotationClient.objects.filter(state=1,
                                                      client=client)
    response = [
        QuotationClientSerializer(qc, context={'request': request}).data
        for qc in quotation_client]
    return response


def lenClient() -> int:
    client = list(Client.objects.filter(state=1))
    return len(client)

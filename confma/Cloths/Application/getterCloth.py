from typing import List

from rest_framework.request import Request

from ...Cloths.Domain.ModelCloth import Cloth
from ...Quotations.Domain.ModelQuotation import Quotation
from ...Quotations.Infrastructure.SerializerQuotation import \
    QuotationSerializer
from ...Rentals.Domain.ModelRental import Rental
from ...Rentals.Infrastructure.SerializerRental import RentalSerializer


def getClothQuotation(cloth: Cloth, request: Request) -> List:
    response = [
        QuotationSerializer(
            q, context={'request': request}
        ).data for q in Quotation.objects.all().filter(state=1,
                                                       cloth=cloth)
    ]
    return response


def getClothRental(cloth: Cloth, request: Request) -> List:
    response = [
        RentalSerializer(
            rental, context={'request': request}
        ).data for rental in Rental.objects.all().filter(state=1,
                                                         cloth=cloth)
    ]
    return response

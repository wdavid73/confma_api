from confma_api.confma.Quotations.Domain.ModelQuotation import Quotation
from confma_api.confma.Quotations.Infrastructure.SerializerQuotation import QuotationSerializer
from confma_api.confma.Quotations.Domain.ModelQuotation import Rental
from confma_api.confma.Rentals.Infrastructure.SerializerRental import RentalSerializer


def getClothQuotation(cloth, request):
    response = [QuotationSerializer(q, context={
        'request': request}).data for q in
                Quotation.objects.all().filter(state=1, cloth=cloth)]
    return response


def getClothRental(cloth, request):
    response = [
        RentalSerializer(rental, context={'request': request}).data for
        rental in
        Rental.objects.all().filter(state=1, cloth=cloth)]
    return response

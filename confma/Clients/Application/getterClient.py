from confma_api.confma.Quotations.Domain.ModelQuotation import Client, QuotationClient, Rental
from confma_api.confma.serializers.quotation_client import \
    QuotationClientSerializer
from confma_api.confma.Rentals.Infrastructure.SerializerRental import RentalSerializer


def getRentalClient(client, request):
    response = [
        RentalSerializer(rental, context={'request': request}).data for
        rental in
        Rental.objects.all().filter(state=1, client=client)]
    return response


def getQuotationClient(client, request):
    quotation_client = QuotationClient.objects.filter(state=1,
                                                      client=client)
    response = [
        QuotationClientSerializer(qc, context={'request': request}).data
        for qc in quotation_client]
    return response


def lenClient():
    client = list(Client.objects.filter(state=1))
    return len(client)

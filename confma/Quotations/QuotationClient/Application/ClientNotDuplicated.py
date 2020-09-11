from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ...Domain.ModelQuotation import Quotation, QuotationClient
from ....Clients.Domain.ModelClient import Client
from ....Clients.Infractructure.SerializerClient import ClientSerializer


@api_view(['GET'])
def ClientNotDuplicatedInQuotation(request, _id):
    quotation = Quotation.objects.filter(id=_id)
    quotation_client = QuotationClient.objects.filter(
        quotation__in=list(quotation))
    list_client = [qc.client.id for qc in quotation_client]
    query_client = Client.objects.exclude(id__in=list_client).filter(
        state=1)
    response = [
        ClientSerializer(client, context={'request': request}).data for
        client in query_client]
    return Response({'clients': response}, status=status.HTTP_200_OK)

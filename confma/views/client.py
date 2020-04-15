from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Client, QuotationClient
from ..serializers.client import ClientSerializer
from ..serializers.quotation_client import QuotationClientSerializer


class ClientViews(APIView):

    def get(self, request):
        clients = Client.objects.filter(state=1)
        serializer = ClientSerializer(
            clients, many=True, context={'request': request})
        return Response({"clients": serializer.data})

    def post(self, request):
        serializer = ClientSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(APIView):

    def get(self, request, id):
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(client, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(
            client, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        client = get_object_or_404(Client, id=id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        client = get_object_or_404(Client, id=_id)
        client.state = 0
        client.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def FindClient(request, _id):
    if request.method == 'POST':
        client = get_object_or_404(Client, id=_id)
        serializer_client = ClientSerializer(
            client, context={'request': request})
        rentals = getRentalClient(client, request)
        quotations = getQuotationClient(client, request)
        return Response({'client': serializer_client.data,
                         'rentals': rentals, 'quotations': quotations})
    return Response(status=status.HTTP_400_BAD_REQUEST)


def getRentalClient(client, request):
    from ..models import Rental
    from ..serializers.rental import RentalSerializer
    response = list()
    for rental in Rental.objects.all().filter(state=1, client=client):
        serializer = RentalSerializer(rental, context={'request': request})
        response.append(serializer.data)
    return response


def getQuotationClient(client, request):
    quotation_client = QuotationClient.objects.filter(state=1, client=client)
    response = []
    for qc in quotation_client:
        serializer = QuotationClientSerializer(
            qc, context={'request': request})
        response.append(serializer.data)
    return response

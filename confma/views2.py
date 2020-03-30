from rest_framework import viewsets

from .models import Rental, QuotationClient, Quotation, Cloth, Client
from .serializers import client, cloth, rental, quotation, quotation_client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(state=1)
    serializer_class = client.ClientSerializer


class ClothViewSet(viewsets.ModelViewSet):
    queryset = Cloth.objects.filter(state=1)
    serializer_class = cloth.ClothSerializer


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.filter(state=1)
    serializer_class = quotation.QuotationSerializer


class QuotationClientViewSet(viewsets.ModelViewSet):
    queryset = QuotationClient.objects.filter(state=1)
    serializer_class = quotation_client.QuotationClientSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.filter(state=1)
    serializer_class = rental.RentalSerializer

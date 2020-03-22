from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client, Rental, QuotationClient, Quotation, Cloth
from .serializers2 import ClientSerializer, ClothSerializer, RentalSerializer, \
    QuotationClientSerializer, QuotationSerializer


@api_view(['POST'])
def delete_log(request, id):
    if request.method == 'POST':
        return Response({'message': 'DELETE LOG IN POST', 'id': id})
    else:
        return Response({'message': 'NOTHING'})


class ClientList(APIView):
    def get(self, request):
        clients = Client.objects.filter(state=1)
        serializer = ClientSerializer(clients, many=True, context={'request': request})
        return Response({"clients": serializer.data})

    def post(self, request):
        print("POST")
        message = "POST"
        return Response({'message': message, 'request': request})

    def put(self, request):
        message = "PUT"
        return Response({'message': message})

    def delete(self, request):
        message = "DELETE PERMANENT"
        return Response({'message': message})


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(state=1)
    serializer_class = ClientSerializer


class ClothViewSet(viewsets.ModelViewSet):
    queryset = Cloth.objects.filter(state=1)
    serializer_class = ClothSerializer


class QuotationViewSet(viewsets.ModelViewSet):
    queryset = Quotation.objects.filter(state=1)
    serializer_class = QuotationSerializer


class QuotationClientViewSet(viewsets.ModelViewSet):
    queryset = QuotationClient.objects.filter(state=1)
    serializer_class = QuotationClientSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.filter(state=1)
    serializer_class = RentalSerializer

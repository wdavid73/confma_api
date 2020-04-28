from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Rental, Cloth
from ..serializers.rental import RentalSerializer,ClothSerializer


class RentalView(APIView):
    def get(self, request):
    	rentals = Rental.objects.filter(state=1,ifrental=1)
    	serializer = RentalSerializer(rentals, many=True, context={'request': request})
    	return Response({'rentals': serializer.data})

    def post(self, request):
        now = datetime.today()
        date_object = datetime.strptime(request.data["date_return"], '%Y-%m-%d')
        if  date_object > now and int(request.data["price"]) > 5000:
            serializer = RentalSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalDetailView(APIView):

    def get(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        serializer = RentalSerializer(rental, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        serializer = RentalSerializer(rental, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rental = get_object_or_404(Rental, id=id)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        rental = get_object_or_404(Rental, id=_id)
        rental.state = 0
        rental.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def RefundRental(request, _id):
    rental = get_object_or_404(Rental, id=_id)
    if request.method == 'POST':
        rental.ifrental = 0
        rental.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def IfNotRental(request):
    rental = Rental.objects.filter(ifrental=0)
    serializer = RentalSerializer(rental, many=True, context={'request': request})
    return Response({'rental':serializer.data} , status=status.HTTP_200_OK)

@api_view(['GET'])
def ClothWithOutRental(request):
    clothwithrental = Rental.objects.filter(state = 1, ifrental=1)
    cloths_id = []
    response = []
    for cr in clothwithrental:
        cloths_id.append(cr.cloth.id)
    cloth = Cloth.objects.exclude(id__in = cloths_id)
    for c in cloth:
        serializer = ClothSerializer(c , context={'request' : request})
        response.append(serializer.data)
    return Response({'response' : response} , status=status.HTTP_200_OK)


	

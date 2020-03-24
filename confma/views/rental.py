from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Rental
from ..serializers.rental import RentalSerializer


class RentalView(APIView):
    def get(self, request):
        rentals = Rental.objects.filter(state=1)
        serializer = RentalSerializer(rentals, many=True, context={'request': request})
        print(serializer)
        return Response({'rentals': serializer.data})

    def post(self, request):
        serializer = RentalSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentalDetailView(APIView):
    def get_object(self, _id):
        try:
            return Rental.objects.get(id=_id)
        except Rental.DoesNotExist:
            raise Http404

    def get(self, request, _id):
        rental = self.get_object(_id)
        serializer = RentalSerializer(rental, context={'request': request})
        return Response(serializer.data)

    def put(self, request, _id):
        rental = self.get_object(_id)
        serializer = RentalSerializer(rental, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        rental = self.get_object(_id)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        rental = get_object_or_404(Rental, id=_id)
        rental.state = 0
        rental.save()
        return Response({'message': 'Delete Successfully'})
    return Response(status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelRental import Rental
from ..Infrastructure.SerializerRental import RentalSerializer


class PutAndDeleteRental(APIView):

    def get(self, request: Request, id: int) -> Response:
        rental = get_object_or_404(Rental, id=id)
        serializer = RentalSerializer(rental,
                                      context={'request': request})
        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        rental = get_object_or_404(Rental, id=id)
        serializer = RentalSerializer(rental, data=request.data,
                                      context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        rental = get_object_or_404(Rental, id=id)
        rental.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

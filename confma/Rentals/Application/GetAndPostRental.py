from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelRental import Rental
from ..Infrastructure.SerializerRental import RentalSerializer


class GetAndPostRental(APIView):
    def get(self, request):
        rentals = Rental.objects.filter(state=1, ifrental=1)
        serializer = RentalSerializer(rentals, many=True,
                                      context={'request': request})
        return Response({'rentals': serializer.data})

    def post(self, request):
        now = datetime.today()
        date_object = datetime.strptime(request.data["date_return"],
                                        '%Y-%m-%d')
        serializer = RentalSerializer(data=request.data,
                                      context={'request': request})
        if serializer.is_valid():
            if date_object > now and int(request.data["price"]) > 5000:
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

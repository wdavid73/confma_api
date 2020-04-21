from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Cloth
from ..serializers.cloth import ClothSerializer


class ClothView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        cloths = Cloth.objects.filter(state=1)
        serializer = ClothSerializer(
            cloths, many=True, context={'request': request})
        return Response({"cloths": serializer.data})

    def post(self, request):
        serializer = ClothSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothDetailView(APIView):
    def get_object(self, id):
        try:
            print(Cloth.objects.get(id=id))
            return Cloth.objects.get(id=id)
        except Cloth.DoesNotExist:
            raise Http404

    def get(self, request, id):
        cloth = self.get_object(id)
        serializer = ClothSerializer(cloth, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        cloth = get_object_or_404(Cloth, id)
        serializer = ClothSerializer(
            cloth, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        cloth = get_object_or_404(Cloth, id)
        # cloth.state = 0
        # cloth.save()
        cloth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def delete_log(request, id):
    if request.method == 'POST':
        cloth = get_object_or_404(Cloth, id=id)
        cloth.state = 0
        cloth.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def DetailsCloth(request, _id):
    if request.method == 'POST':
        cloth = get_object_or_404(Cloth, id=_id)
        serializer_cloth = ClothSerializer(cloth, context={'request': request})
        quotation = getClothQuotation(cloth, request)
        rental = getClothRental(cloth, request)
        return Response(
            {
                'cloth': serializer_cloth.data,
                'quotation': quotation,
                'rentals': rental
            },
            status=status.HTTP_200_OK)

    return Response(status=status.HTTP_400_BAD_REQUEST)


def getClothQuotation(cloth, request):
    from ..models import Quotation
    from ..serializers.quotation import QuotationSerializer
    response = list()
    for q in Quotation.objects.all().filter(state=1, cloth=cloth):
        serializer = QuotationSerializer(q, context={'request': request})
        response.append(serializer.data)
    return response


def getClothRental(cloth, request):
    from ..models import Rental
    from ..serializers.rental import RentalSerializer
    response = list()
    for rental in Rental.objects.all().filter(state=1, cloth=cloth):
        serializer = RentalSerializer(rental, context={'request': request})
        response.append(serializer.data)
    return response

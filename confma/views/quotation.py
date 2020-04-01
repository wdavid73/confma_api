from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Quotation, Cloth
from ..serializers.quotation import QuotationSerializer


class QuotationView(APIView):
    def get(self, request):
        quotation = Quotation.objects.filter(state=1)
        serializer = QuotationSerializer(quotation, many=True, context={'request': request})
        return Response({"quotation": serializer.data})

    def post(self, request):
        if not ClothDuplicated(request.data['cloth']):
            serializer = QuotationSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Cloth Duplicated in Quotations'}, status=status.HTTP_400_BAD_REQUEST)


class QuotationDetailView(APIView):

    def get(self, request, id):
        quotation = get_object_or_404(Quotation, id=id)
        serializer = QuotationSerializer(quotation, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        quotation = get_object_or_404(Quotation, id=id)
        serializer = QuotationSerializer(quotation, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        quotation = get_object_or_404(Quotation, id=id)
        quotation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        quotation = get_object_or_404(Quotation, id=_id)
        quotation.state = 0
        quotation.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


def total(querydict, total=0):
    for data in querydict:
        if data != 'cloth':
            total += int(querydict[data])
    return total


@api_view(['POST'])
def FindQuotations(request, cloth_name):
    cloths = FindClothByName(cloth_name, request)
    quotations = Quotation.objects.filter(cloth__in=list(cloths))
    return Response(status=status.HTTP_200_OK)


def FindClothByName(cloth_name, request):
    cloth = Cloth.objects.filter(name=cloth_name, id__in=list(ClothWithOutQuotation().values_list('id', flat=True)))
    return cloth


def ClothWithOutQuotation():
    quotations = Quotation.objects.filter(state=1).values_list('cloth', flat=True)
    cloth_quotation = Cloth.objects.exclude(id__in=quotations)
    return cloth_quotation


def ClothDuplicated(req):
    cloth = Cloth.objects.filter(id=req)
    if Quotation.objects.filter(cloth__in=list(cloth)):
        return True

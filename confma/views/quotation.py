from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Quotation
from ..serializers.quotation import QuotationSerializer


class QuotationView(APIView):
    def get(self, request):
        quotation = Quotation.objects.filter(state=1)
        serializer = QuotationSerializer(quotation, many=True, context={'request': request})
        return Response({"quotation": serializer.data})

    def post(self, request):
        serializer = QuotationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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

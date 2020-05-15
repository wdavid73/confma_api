from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelQuotation import Quotation
from ..Infrastructure.SerializerQuotation import QuotationSerializer


class PutAndDelete(APIView):

    def get(self, request, id):
        quotation = get_object_or_404(Quotation, id=id)
        serializer = QuotationSerializer(
            quotation, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        quotation = get_object_or_404(Quotation, id=id)
        serializer = QuotationSerializer(
            quotation, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        quotation = get_object_or_404(Quotation, id=id)
        quotation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

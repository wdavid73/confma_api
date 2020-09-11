from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ...Domain.ModelQuotation import QuotationClient
from ..Infractructure.SerializerQuotationClient import \
    QuotationClientSerializer


class PutAndDeleteQuotationClient(APIView):

    def get(self, request, id):
        qc = get_object_or_404(QuotationClient, id=id)
        serializer = QuotationClientSerializer(qc, context={
            'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        qc = get_object_or_404(QuotationClient, id=id)
        serializer = QuotationClientSerializer(qc, data=request.data,
                                               context={
                                                   'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        qc = get_object_or_404(QuotationClient, id=id)
        qc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

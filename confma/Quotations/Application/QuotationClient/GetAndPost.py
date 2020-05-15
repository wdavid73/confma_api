from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...Infrastructure.SerializerQuotationClient import \
    QuotationClientSerializer
from ...Domain.ModelQuotation import QuotationClient


class GetAndPostQuotationClient(APIView):

    def get(self, request):
        qc = QuotationClient.objects.filter(state=1)
        serializer = QuotationClientSerializer(qc, many=True, context={
            'request': request})
        return Response({'Quotation_Client': serializer.data})

    def post(self, request):
        serializer = QuotationClientSerializer(data=request.data,
                                               context={
                                                   'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
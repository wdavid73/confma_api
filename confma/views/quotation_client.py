from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import QuotationClient
from ..serializers.quotation_client import QuotationClientSerializer


class QuotationClientViewSet(viewsets.ModelViewSet):
    queryset = QuotationClient.objects.filter(state=1)
    serializer_class = QuotationClientSerializer


class QuotationClientView(APIView):

    def get(self, request):
        qc = QuotationClient.objects.filter(state=1)
        serializer = QuotationClientSerializer(qc, many=True, context={'request': request})
        return Response({'Quotation Client': serializer.data})

    def post(self, request):
        serializer = QuotationClientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuotationClientDetailView(APIView):

    def get(self, request, id):
        qc = get_object_or_404(QuotationClient, id=id)
        serializer = QuotationClientSerializer(qc, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        qc = get_object_or_404(QuotationClient, id=id)
        serializer = QuotationClientSerializer(qc, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        qc = get_object_or_404(QuotationClient, id=id)
        qc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        qc = get_object_or_404(QuotationClient, id=_id)
        qc.state = 0
        qc.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

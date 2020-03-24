from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Quotation
from ..serializers.quotation import QuotationSerializer


class QuotationView(APIView):
    def get(self, request):
        print("GET")
        quotation = Quotation.objects.filter(state=1)
        serializer = QuotationSerializer(quotation, many=True, context={'request': request})
        return Response({"quotation": serializer.data})

    def post(self, request):
        serializer = QuotationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class QuotationDetailView(APIView):
    def get_object(self, _id):
        try:
            return Quotation.objects.get(id=_id)
        except Quotation.DoesNotExist:
            raise Http404

    def get(self, request, _id):
        quotation = self.get_object(_id)
        serializer = QuotationSerializer(quotation, context={'request': request})
        return Response(serializer.data)

    def put(self, request, _id):
        quotation = self.get_object(_id)
        serializer = QuotationSerializer(quotation, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        quotation = self.get_object(_id)
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

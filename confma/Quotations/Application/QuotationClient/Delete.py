from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ...Domain.ModelQuotation import QuotationClient


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        qc = get_object_or_404(QuotationClient, id=_id)
        qc.state = 0
        qc.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..Domain.ModelQuotation import Quotation
from ..Infrastructure.SerializerQuotation import QuotationSerializer


@api_view(["GET"])
def GetOneQuotation(request: Request, _id: int) -> Response:
    quotation = get_object_or_404(Quotation, id=_id)
    serializer = QuotationSerializer(quotation, context={"request": request})
    return Response({"quotation": serializer.data})

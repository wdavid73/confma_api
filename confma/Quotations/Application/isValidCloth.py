from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from ...Cloths.Domain.ModelCloth import Cloth
from ..Domain.ModelQuotation import Quotation


class isValidCloth(APIView):
    def get(self, request: Request, id: int) -> Response:
        cloth = Cloth.objects.get(id=id)
        if Quotation.objects.filter(cloth=cloth).exists():
            return Response({"valid": False})
        else:
            return Response({"valid": True})

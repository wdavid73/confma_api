from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from ..Domain.ModelQuotation import Quotation
from ...Cloths.Domain.ModelCloth import Cloth


def ClothDuplicated(req):
    cloth = Cloth.objects.filter(id=req)
    if len(Quotation.objects.filter(cloth__in=list(cloth))) > 0:
        return True
    return False


@api_view(['GET'])
def isValidCloth(request: Request, id: int) -> Response:
    cloth = Cloth.objects.get(id=id)
    if Quotation.objects.filter(cloth=cloth).exists():
        return Response({"valid": False})
    else:
        return Response({"valid": True})



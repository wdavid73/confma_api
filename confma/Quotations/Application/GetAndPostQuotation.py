from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelQuotation import Quotation
from ..Infractructure.SerializerQuotation import QuotationSerializer
from ...Cloths.Domain.ModelCloth import Cloth


class GetAndPost(APIView):

    def get(self, request: Request) -> Response:
        quotation = Quotation.objects.filter(state=1)
        serializer = QuotationSerializer(
            quotation, many=True, context={'request': request})
        return Response({"quotations": serializer.data})

    def post(self, request: Request):
        if request.data["clothId"] == None:
            if not ClothDuplicated(request.data['clothId']):
                total = getTotal(request.data)
                request.data._mutable = True
                request.data['total'] = str(total)
                request.data._mutable = False
                serializer = QuotationSerializer(
                    data=request.data, context={'request': request})
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,
                                    status=status.HTTP_201_CREATED)
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': ['Esta prenda ya ah sido cotizada']},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({'error': ['peticion invalida']}, status=status.HTTP_400_BAD_REQUEST)


def ClothDuplicated(req):
    cloth = Cloth.objects.filter(id=req)
    if len(Quotation.objects.filter(cloth__in=list(cloth))) > 0:
        return True
    return False


def getTotal(data):
    return (
        int(data['value_work']) +
        int(data['value_cloth']) +
        int(data['value_buttons']) +
        int(data['value_threads']) +
        int(data['value_necks']) +
        int(data['value_embroidery']) +
        int(data['value_prints'])
    )

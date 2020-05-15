from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelQuotation import Quotation
from ...Cloths.Domain.ModelCloth import Cloth
from ..Infrastructure.SerializerQuotation import QuotationSerializer


class GetAndPost(APIView):

    def get(self, request):
        quotation = Quotation.objects.filter(state=1)
        serializer = QuotationSerializer(
            quotation, many=True, context={'request': request})
        return Response({"quotations": serializer.data})

    def post(self, request):
        if not ClothDuplicated(request.data['clothId']):
            total = getTotal(
                request.data['value_work'], request.data['value_cloth'],
                request.data['value_buttons'],
                request.data['value_threads'],
                request.data['value_necks'],
                request.data['value_embroidery'],
                request.data['value_prints'])
            request.data['total'] = str(total)
            serializer = QuotationSerializer(
                data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Esta prenda ya ah sido cotizada'},
                        status=status.HTTP_406_NOT_ACCEPTABLE)


def ClothDuplicated(req):
    cloth = Cloth.objects.filter(id=req)
    if len(Quotation.objects.filter(cloth__in=list(cloth))) > 0:
        return True
    return False


def getTotal(vw, vc, vb, vt, vn, ve, vp):
    return int(vw) + int(vc) + int(vb) + int(vt) + int(vn) + int(
        ve) + int(vp)

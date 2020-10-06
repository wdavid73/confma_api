from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniformFemale import UniformsFemale
from ..Infractructure.SerializerUniformFemale import UniformFemaleSerializer

from ...Dresses.Domain.ModelDresses import DressesUniform
from ...Shirts.Domain.ModelShirts import Shirts


class GetAndPost(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request: Request) -> Response:
        uniforms = UniformsFemale.objects.filter(state=1)
        serializer = UniformFemaleSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms_female': serializer.data})

    def post(self, request: Request):
        price = getPriceTotal(
            request.data["dress_id"],
            request.data["shirt_id"],
            request.data["pants_id"]
        )
        # PERMITE MODIFICAR O MUTAR CUALQUIER ATRIBUTO DEL QUERYDICT
        request.data._mutable = True
        request.data['price'] = price
        # BLOQUEA MODIFICAR O MUTAR CUALQUIER ATRIBUTO DEL QUERYDICT
        request.data._mutable = False
        serializer = UniformFemaleSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def getPriceTotal(dress_id, shirt_id, pants_id):
    shirt = get_object_or_404(Shirts, id=shirt_id)
    dress = get_object_or_404(DressesUniform, id=dress_id)
    return dress.price + shirt.price

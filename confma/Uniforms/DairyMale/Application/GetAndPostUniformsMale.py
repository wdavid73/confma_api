from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response
from ..Domain.ModelUniformMale import UniformsMale
from ..Infractructure.SerializerUniformMale import UniformMaleSerializer
from ...Pants.Domain.ModelPants import Pants
from ...Shirts.Domain.ModelShirts import Shirts


class GetAndPost(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request: Request):
        uniforms = UniformsMale.objects.filter(state=1)
        serializer = UniformMaleSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms_male': serializer.data})

    def post(self, request: Request):
        price = getPriceTotal(
            request.data["pants_id"],
            request.data["shirt_id"]
        )
        # PERMITE MODIFICAR O MUTAR CUALQUIER ATRIBUTO DEL QUERYDICT
        request.data._mutable = True
        request.data['price'] = price
        # BLOQUEA MODIFICAR O MUTAR CUALQUIER ATRIBUTO DEL QUERYDICT
        request.data._mutable = False
        serializer = UniformMaleSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def getPriceTotal(pants_id, shirt_id):
    pants = get_object_or_404(Pants, id=pants_id)
    shirt = get_object_or_404(Shirts, id=shirt_id)
    return pants.price + shirt.price

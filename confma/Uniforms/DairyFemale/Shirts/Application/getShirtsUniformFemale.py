from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelShirtsUniformFemale import ShirtsUniformFemale
from ..Infrastructure.SerializerShirstFemale import ShirstFemaleSerializer


class GetShirtsUniformFemale(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        shirts = ShirtsUniformFemale.objects.filter(state=1)
        serializer = ShirstFemaleSerializer(
            shirts, many=True, context={'request': request})
        return Response({'dresses': serializer.data})

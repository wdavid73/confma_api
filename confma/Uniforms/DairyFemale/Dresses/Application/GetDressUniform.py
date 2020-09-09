from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelDresses import DressesUniform
from ..Infrastructure.SerializerDresses import DressSerializer


class GetDressUniform(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        dresses = DressesUniform.objects.filter(state=1)
        serializer = DressSerializer(
            dresses, many=True, context={'request': request})
        return Response({'dresses': serializer.data})

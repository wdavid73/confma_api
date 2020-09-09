from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelShirtsUniformMale import ShirtsUniformMale
from ..Infrastructure.SerializerShirstMale import ShirtsMaleSerializer


class GetShirtsUniformFemale(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        shirts = ShirtsUniformMale.objects.filter(state=1)
        serializer = ShirtsMaleSerializer(
            shirts, many=True, context={'request': request})
        return Response({'dresses': serializer.data})

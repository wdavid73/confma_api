from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelShirtsUniformSports import ShirtsUniformSports
from ..Infrastructure.SerializerShirstSport import ShirtsSportsSerializer


class GetShirtsUniformSports(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        shirts = ShirtsUniformSports.objects.filter(state=1)
        serializer = ShirtsSportsSerializer(
            shirts, many=True, context={'request': request})
        return Response({'shirts_sports': serializer.data})

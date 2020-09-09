from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelSweatShirtUniformSports import SweatShirtUniformSports
from ..Infrastructure.SerializerSweatShirtSport import SweatShirtSportsSerializer


class GetSweatShirtUniformSports(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        shirts = SweatShirtUniformSports.objects.filter(state=1)
        serializer = SweatShirtSportsSerializer(
            shirts, many=True, context={'request': request})
        return Response({'sweatshirt_sports': serializer.data})

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..domain.ModelShields import Shields
from ..infractructure.ShieldsSerializer import ShieldsSerializer


class GetShields(APIView):
    parser_class = (FileUploadParser)

    def get(self, request: Request) -> Response:
        shields = Shields.objects.filter(state=1)
        serializer = ShieldSerializer(
            shields, many=True, context={'request': request})
        return Response({'shields': serializer.data})

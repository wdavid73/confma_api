from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniformSports import UniformsSports
from ..Infractructure.SerializerUniformSports import UniformSportsSerializer


class GetUniformSports(APIView):
    parser_class = (FileUploadParser)

    def get(self, request: Request) -> Response:
        uniforms = UniformsSports.objects.filter(state=1)
        serializer = UniformSportsSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms_sports': serializer.data})

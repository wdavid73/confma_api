from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniform import Uniforms
from ..Infractructure.SerializerUniform import UniformSerializer


class GetUniform(APIView):
    parser_class = (FileUploadParser)

    def get(self, request: Request) -> Response:
        uniforms = Uniforms.objects.filter(state=1)
        serializer = UniformSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms': serializer.data})

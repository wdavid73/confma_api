from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniformMale import UniformsMale
from ..Infractructure.SerializerUniformMale import UniformMaleSerializer


class GetUniformsMale(APIView):
    parser_class = (FileUploadParser)

    def get(self, request: Request) -> Response:
        uniforms = UniformsMale.objects.filter(state=1)
        serializer = UniformMaleSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms_male': serializer.data})

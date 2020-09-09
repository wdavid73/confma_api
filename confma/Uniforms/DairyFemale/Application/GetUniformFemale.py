from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniformFemale import UniformsFemale
from ..Infractructure.SerializerUniformFemale import UniformFemaleSerializer


class GetUniformFemale(APIView):
    parser_class = (FileUploadParser)

    def get(self, request: Request) -> Response:
        uniforms = UniformsFemale.objects.filter(state=1)
        serializer = UniformFemaleSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms': serializer.data})

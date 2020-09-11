from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniformMale import UniformsMale
from ..Infractructure.SerializerUniformMale import UniformMaleSerializer


class GetAndPost(APIView):
    parser_class = (FileUploadParser)

    def get(self, request: Request) -> Response:
        uniforms = UniformsMale.objects.filter(state=1)
        serializer = UniformMaleSerializer(
            uniforms, many=True, context={'request': request})
        return Response({'uniforms_male': serializer.data})

    def post(self, request: Request) -> Response:
        serializer = UniformMaleSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
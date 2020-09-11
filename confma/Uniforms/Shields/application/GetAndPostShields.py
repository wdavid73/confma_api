from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..domain.ModelShields import Shields
from ..infractructure.ShieldsSerializer import ShieldsSerializer


class GetAndPost(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        shields = Shields.objects.filter(state=1)
        serializer = ShieldsSerializer(
            shields, many=True, context={'request': request})
        return Response({'shields': serializer.data})

    def post(self, request: Request) -> Response:
        serializer = ShieldsSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
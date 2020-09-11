from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelShirtsSports import ShirtsSports
from ..Infractructure.SerializerShirstSport import ShirtsSportsSerializer


class GetAndPost(APIView):
    parser_class = FileUploadParser

    def get(self, request: Request) -> Response:
        shirts = ShirtsSports.objects.filter(state=1)
        serializer = ShirtsSportsSerializer(
            shirts, many=True, context={'request': request})
        return Response({'shirts_sports': serializer.data})

    def post(self, request: Request) -> Response:
        serializer = ShirtsSportsSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
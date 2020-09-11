from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelShirtsFemale import ShirtsFemale
from ..Infrastructure.SerializerShirstFemale import ShirtsFemaleSerializer


class GetAndPost(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request: Request) -> Response:
        shirts = ShirtsFemale.objects.filter(state=1)
        serializer = ShirtsFemaleSerializer(
            shirts, many=True, context={'request': request})
        return Response({'shirts_female': serializer.data})

    def post(self, request: Request) -> Response:
        serializer = ShirtsFemaleSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

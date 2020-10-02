from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelPantsMale import PantsMale
from ..Infrastructure.SerializerPantsMale import PantsMaleSerializer


class GetPantsUniformMale(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request: Request) -> Response:
        shirts = PantsMale.objects.filter(state=1)
        serializer = PantsMaleSerializer(
            shirts, many=True, context={'request': request})
        return Response({'pants_male': serializer.data})

    def post(self, request: Request) -> Response:
        serializer = PantsMaleSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
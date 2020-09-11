from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelCloth import Cloth
from ..Infrastruture.SerializerCloth import ClothSerializer


class GetAndPost(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request : Request) -> Response:
        cloths = Cloth.objects.filter(state=1)
        serializer = ClothSerializer(cloths, many=True,
                                     context={'request': request})
        return Response({"cloths": serializer.data})

    def post(self, request: Request) -> Response:
        serializer = ClothSerializer(data=request.data,
                                     context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

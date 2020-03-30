from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Cloth
from ..serializers.cloth import ClothSerializer


@api_view(['POST'])
def delete_log(request, id):
    if request.method == 'POST':
        cloth = get_object_or_404(Cloth, id=id)
        cloth.state = 0
        cloth.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class ClothView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        cloths = Cloth.objects.filter(state=1)
        serializer = ClothSerializer(cloths, many=True, context={'request': request})
        return Response({"cloths": serializer.data})

    def post(self, request):
        serializer = ClothSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClothDetailView(APIView):
    def get(self, request, id):
        cloth = get_object_or_404(Cloth, id)
        serializer = ClothSerializer(cloth, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        cloth = get_object_or_404(Cloth, id)
        serializer = ClothSerializer(cloth, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        cloth = get_object_or_404(Cloth, id)
        # cloth.state = 0
        # cloth.save()
        cloth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

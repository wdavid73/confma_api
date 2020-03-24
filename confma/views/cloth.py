from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Cloth
from ..serializers.cloth import ClothSerializer


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        cloth = get_object_or_404(Cloth, id=_id)
        cloth.state = 0
        cloth.save()
        return Response({'message': 'Delete Successfully'})
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
    def get_object(self, _id):
        try:
            print(Cloth.objects.get(id=_id))
            return Cloth.objects.get(id=_id)
        except Cloth.DoesNotExist:
            raise Http404

    def get(self, request, _id):
        Cloth = self.get_object(_id)
        serializer = ClothSerializer(Cloth, context={'request': request})
        return Response(serializer.data)

    def put(self, request, _id):
        cloth = self.get_object(_id)
        serializer = ClothSerializer(cloth, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        cloth = self.get_object(_id)
        # cloth.state = 0
        # cloth.save()
        cloth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

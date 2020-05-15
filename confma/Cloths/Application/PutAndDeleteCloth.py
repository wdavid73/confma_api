from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelCloth import Cloth
from ..Infrastruture.SerializerCloth import ClothSerializer


class PutAndDeleteCloth(APIView):
    def get_object(self, id):
        try:
            print(Cloth.objects.get(id=id))
            return Cloth.objects.get(id=id)
        except Cloth.DoesNotExist:
            raise Http404

    def get(self, request, id):
        cloth = self.get_object(id)
        serializer = ClothSerializer(cloth, context={'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        cloth = get_object_or_404(Cloth, id)
        serializer = ClothSerializer(
            cloth, data=request.data, context={'request': request})
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


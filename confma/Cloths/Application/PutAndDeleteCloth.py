from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelCloth import Cloth
from ..Infrastruture.SerializerCloth import ClothSerializer


class PutAndDelete(APIView):
    def get_object(self, id: int) -> Cloth:
        try:
            return Cloth.objects.get(id=id)
        except Cloth.DoesNotExist:
            raise Http404

    def put(self, request: Request, id: int) -> Response:
        cloth = self.get_object(id)
        serializer = ClothSerializer(cloth, data=request.data,
                                     context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, _id: int) -> Response:
        cloth = self.get_object(_id)
        cloth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

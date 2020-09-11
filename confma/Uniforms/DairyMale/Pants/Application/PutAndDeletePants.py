from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from ..Domain.ModelPantsMale import PantsMale
from ..Infrastructure.SerializerPantsMale import PantsMaleSerializer

class PutAndDelete(APIView):
    def get_object(self, id):
        try:
            return PantsMale.objects.get(id=id)
        except PantsMale.DoesNotExist:
            raise Http404

    def put(self, request: Request, id: int) -> Response:
        uniform_female = self.get_object(id)
        serializer = PantsMaleSerializer(
            uniform_female, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        from .....General.Application.delete import delete
        if delete(PantsMale, id):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
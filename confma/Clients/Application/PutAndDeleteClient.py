from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelClient import Client
from ..Infrastructure.SerializerClient import ClientSerializer


class PutAndDeleteClient(APIView):
    def get_object(self, id):
        try:
            return Client.objects.get(id=id)
        except Client.DoesNotExist:
            raise Http404

    def put(self, request: Request, id: int) -> Response:
        client = self.get_object(id)
        serializer = ClientSerializer(
            client, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id: int) -> Response:
        client = self.get_object(id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

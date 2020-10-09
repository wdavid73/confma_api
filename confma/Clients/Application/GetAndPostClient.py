from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelClient import Client
from ..Infractructure.SerializerClient import ClientSerializer


class GetAndPost(APIView):

    def get(self, request: Request):
        clients = Client.objects.filter(state=1)
        serializer = ClientSerializer(
            clients, many=True, context={'request': request})
        return Response({"clients": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = ClientSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

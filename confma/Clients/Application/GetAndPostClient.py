from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelClient import Client
from ..Infrastructure.SerializerClient import ClientSerializer


class GetAndPostClient(APIView):

    def get(self, request: Request) -> Response:
        clients = Client.objects.filter(state=1)
        serializer = ClientSerializer(
            clients, many=True, context={'request': request})
        return Response({"clients": serializer.data})

    def post(self, request: Request) -> Response:
        serializer = ClientSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

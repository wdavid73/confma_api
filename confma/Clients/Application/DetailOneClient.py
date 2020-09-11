from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ..Domain.ModelClient import Client
from ..Infractructure.SerializerClient import ClientSerializer


class DetailOneClient(APIView):
    def get(self, request: Request, id: int) -> Response:
        client = get_object_or_404(Client, id=id)
        serializer = ClientSerializer(client, context={"request": request})
        return Response({"client": serializer.data})

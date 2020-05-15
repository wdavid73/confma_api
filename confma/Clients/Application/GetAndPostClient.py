from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Infrastructure.SerializerClient import ClientSerializer
from ..Domain.ModelClient import Client


class GetAndPostClient(APIView):

    def get(self, request):
        clients = Client.objects.filter(state=1)
        serializer = ClientSerializer(
            clients, many=True, context={'request': request})
        return Response({"clients": serializer.data})

    def post(self, request):
        serializer = ClientSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

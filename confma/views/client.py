from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Client
from ..serializers.client import ClientSerializer


@api_view(['POST'])
def delete_log(request, _id):
    if request.method == 'POST':
        client = get_object_or_404(Client, id=_id)
        client.state = 0
        client.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class ClientViews(APIView):

    def get(self, request):
        clients = Client.objects.filter(state=1)
        serializer = ClientSerializer(clients, many=True, context={'request': request})
        return Response({"clients": serializer.data})

    def post(self, request):
        serializer = ClientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetailView(APIView):
    def get_object(self, _id):
        try:
            print(Client.objects.get(id=_id))
            return Client.objects.get(id=_id)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, _id):
        client = self.get_object(_id)
        serializer = ClientSerializer(client, context={'request': request})
        return Response(serializer.data)

    def put(self, request, _id):
        client = self.get_object(_id)
        serializer = ClientSerializer(client, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, _id):
        client = self.get_object(_id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

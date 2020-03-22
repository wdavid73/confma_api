from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Client
from ..serializers.client import ClientSerializer


@api_view(['POST'])
def delete_log(request, id):
    if request.method == 'POST':
        return Response({'message': 'DELETE LOG IN POST', 'id': id})
    else:
        return Response({'message': 'NOTHING'})


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

    def put(self, request):
        message = "PUT"
        return Response({'message': message})

    def delete(self, request):
        message = "DELETE PERMANENT"
        return Response({'message': message})

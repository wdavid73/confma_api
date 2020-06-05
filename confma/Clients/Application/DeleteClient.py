from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelClient import Client
from ...General.Application.delete import delete


@api_view(['POST'])
def delete_log(request: Request, _id: int) -> Response:
    if request.method == 'POST':
        delete(Client, _id)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

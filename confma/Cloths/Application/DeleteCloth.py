from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..Domain.ModelCloth import Cloth


@api_view(['POST'])
def delete_log(request, id):
    if request.method == 'POST':
        cloth = get_object_or_404(Cloth, id=id)
        cloth.state = 0
        cloth.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
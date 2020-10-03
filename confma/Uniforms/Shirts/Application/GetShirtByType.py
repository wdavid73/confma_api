from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..Domain.ModelShirts import Shirts
from ..Infrastructure.SerializerShirts import ShirtsSerializer


@api_view(['GET'])
def getShirtsMale(request: Request):
    response = [
        ShirtsSerializer(
            shirt,
            context={'request': request}
        ).data for shirt in Shirts.objects.filter(state=1, type="Male")
    ]
    return Response({'shirts_male': response}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getShirtsFemale(request: Request):
    response = [
        ShirtsSerializer(
            shirt,
            context={'request': request}
        ).data for shirt in Shirts.objects.filter(state=1, type="Female")
    ]
    return Response({'shirts_female': response}, status=status.HTTP_200_OK)

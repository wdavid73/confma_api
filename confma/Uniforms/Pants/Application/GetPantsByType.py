from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..Domain.ModelPants import Pants
from ..Infrastructure.SerializerPants import PantsSerializer


@api_view(['GET'])
def getPantsMale(request: Request):
    response = [
        PantsSerializer(
            pants,
            context={'request': request}
        ).data for pants in Pants.objects.filter(state=1, type="Male")
    ]
    return Response({'pants_male': response}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getPantsFemale(request: Request):
    response = [
        PantsSerializer(
            pants,
            context={'request': request}
        ).data for pants in Pants.objects.filter(state=1, type="Female")
    ]
    return Response({'pants_female': response}, status=status.HTTP_200_OK)

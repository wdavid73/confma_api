from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..Domain.ModelUniformSports import UniformsSports
from ..Infractructure.SerializerUniformSports import UniformSportsSerializer


@api_view(['GET'])
def getMale(request: Request):
    response = [
        UniformSportsSerializer(
            male,
            context={'request': request}
        ).data for male in UniformsSports.objects.filter(state=1, type_uniform="SportMale")
    ]
    return Response({'uniforms_sports_male': response}, status=status.HTTP_200_OK)


@api_view(['GET'])
def getFemale(request: Request):
    response = [
        UniformSportsSerializer(
            female,
            context={'request': request}
        ).data for female in UniformsSports.objects.filter(state=1, type_uniform="SportFemale")
    ]
    return Response({'uniforms_sports_female': response}, status=status.HTTP_200_OK)

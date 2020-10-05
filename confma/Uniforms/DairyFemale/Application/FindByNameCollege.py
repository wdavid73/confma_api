from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..Domain.ModelUniformFemale import UniformsFemale
from ..Infractructure.SerializerUniformFemale import UniformFemaleSerializer
from ....Institution.Domain.Institution import Institution


@api_view(['GET'])
def FindByNameCollege(request: Request, id: int):
    institution = Institution.objects.filter(id=id, state=1)
    uniforms = UniformsFemale.objects.filter(institution__in=list(institution))
    response = [
        UniformFemaleSerializer(
            uniform,
            context={'request': request}
        ).data for uniform in uniforms
    ]
    return Response({"uniform_female": response}, status=status.HTTP_200_OK)

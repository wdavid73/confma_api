from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..Domain.ModelUniformMale import UniformsMale

@api_view(['GET'])
def FindByNameCollege(request: Request, name: str):
    uniforms = UniformsMale.objects.filter(name_college=name)
    print(uniforms)
    print("find by name college")
    HttpResponse("find by name college")
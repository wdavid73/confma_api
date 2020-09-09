from django.urls import path

from ..Application.GetUniform import GetUniform

urlpatterns = [
    path('', GetUniform.as_view(), name="uniforms"),
]

from django.urls import path

from ..Application.GetUniformsMale import GetUniformsMale

urlpatterns = [
    path('', GetUniformsMale.as_view(), name="uniforms"),
]

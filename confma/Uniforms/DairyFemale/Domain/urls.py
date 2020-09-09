from django.urls import path

from ..Application.GetUniformFemale import GetUniformFemale

urlpatterns = [
    path('', GetUniformFemale.as_view(), name="uniforms"),
]

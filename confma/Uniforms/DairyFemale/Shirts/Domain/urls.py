from django.urls import path,include

from ..Application.getShirtsUniformFemale import GetShirtsUniformFemale

urlpatterns = [
    path('', GetShirtsUniformFemale.as_view(), name="get_shirts_female"),
]
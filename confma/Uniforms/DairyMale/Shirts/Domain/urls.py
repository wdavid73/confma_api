from django.urls import path,include

from ..Application.getShirtsUniformMale import GetShirtsUniformFemale

urlpatterns = [
    path('', GetShirtsUniformFemale.as_view(), name="get_shirts_male"),
]
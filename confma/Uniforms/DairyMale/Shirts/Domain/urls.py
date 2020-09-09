from django.urls import path,include

from ..Application.getShirtsUniformMale import GetShirtsUniformMale

urlpatterns = [
    path('', GetShirtsUniformMale.as_view(), name="get_shirts_male"),
]
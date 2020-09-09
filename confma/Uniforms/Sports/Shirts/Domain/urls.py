from django.urls import path,include

from ..Application.getShirtsUniformSports import GetShirtsUniformSports

urlpatterns = [
    path('', GetShirtsUniformSports.as_view(), name="get_shirts_sports"),
]
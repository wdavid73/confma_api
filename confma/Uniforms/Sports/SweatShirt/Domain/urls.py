from django.urls import path,include

from ..Application.getSweatShirtUniformSports import GetSweatShirtUniformSports

urlpatterns = [
    path('', GetSweatShirtUniformSports.as_view(), name="get_sweatshirts_sports"),
]
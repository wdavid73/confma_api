from django.urls import path, include
from ..application.getShields import GetShields

urlpatterns = [
    path('', GetShields.as_view(), name="shields"),

]

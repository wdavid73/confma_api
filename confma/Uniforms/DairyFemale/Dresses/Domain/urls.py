from django.urls import path,include

from ..Application.GetDressUniform import GetDressUniform

urlpatterns = [
    path('', GetDressUniform.as_view(), name="get_dresses"),
]

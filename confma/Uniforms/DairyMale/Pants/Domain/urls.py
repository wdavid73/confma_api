from django.urls import path,include

from ..Application.getPantsUniformMale import GetPantsUniformMale

urlpatterns = [
    path('', GetPantsUniformMale.as_view(), name="get_pants_male"),
]
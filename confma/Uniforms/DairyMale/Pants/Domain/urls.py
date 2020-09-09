from django.urls import path,include

from ..Application.getPantsUniformMale import GetPantsUniformFemale

urlpatterns = [
    path('', GetPantsUniformFemale.as_view(), name="get_pants_male"),
]
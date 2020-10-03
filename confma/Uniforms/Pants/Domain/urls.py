from django.urls import path, include

from ..Application.GetAndPostPants import GetPantsUniformMale
from ..Application.PutAndDeletePants import PutAndDelete
from ..Application.GetPantsByType import getPantsMale, getPantsFemale


urlpatterns = [
    path('', GetPantsUniformMale.as_view(), name="get_pants_male"),
    path('male/', getPantsMale, name="get_pants_male"),
    path('female/', getPantsFemale, name="get_pants_female"),
    path('<id>/', PutAndDelete.as_view(), name="pants_male_detail"),
]

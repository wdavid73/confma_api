from django.urls import path, include

from ..Application.GetAndPostPants import GetPantsUniformMale
from ..Application.PutAndDeletePants import PutAndDelete
from ..Application.GetPantsByType import getPantsMale, getPantsFemale, getPantsSportMale, getPantsSportFemale


urlpatterns = [
    path('', GetPantsUniformMale.as_view(), name="get_pants_male"),
    path('male/', getPantsMale, name="get_pants_male"),
    path('female/', getPantsFemale, name="get_pants_female"),
    path('male/sport/', getPantsSportMale, name="get_pants_sport_male"),
    path('female/sport/', getPantsSportFemale, name="get_pants_sport_female"),
    path('<id>/', PutAndDelete.as_view(), name="pants_male_detail"),
]

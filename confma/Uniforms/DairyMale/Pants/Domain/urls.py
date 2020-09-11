from django.urls import path,include

from ..Application.GetAndPostPants import GetPantsUniformMale
from ..Application.PutAndDeletePants import PutAndDelete


urlpatterns = [
    path('', GetPantsUniformMale.as_view(), name="get_pants_male"),
    path('<id>/', PutAndDelete.as_view(), name="pants_male_detail"),
]
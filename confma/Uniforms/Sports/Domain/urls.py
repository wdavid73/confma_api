from django.urls import path, include

from ..Application.GetAndPostSports import GetAndPost
from ..Application.PutAndDeleteSports import PutAndDelete
from ..Application.GetByType import getMale, getFemale

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms_sports"),
    path('male/', GetAndPost.as_view(), name="uniforms_sports_male"),
    path('female/', GetAndPost.as_view(), name="uniforms_sports_female"),
    path('<id>/', PutAndDelete.as_view(), name="uniform_sports_detail")
]

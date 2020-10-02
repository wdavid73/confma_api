from django.urls import path,include

from ..Application.GetAndPostSports import GetAndPost
from ..Application.PutAndDeleteSports import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="uniforms_sports"),
    path('<id>/',PutAndDelete.as_view() , name="uniform_sports_detail")
]

from django.urls import path, include
from ..application.GetAndPostShields import GetAndPost
from ..application.PutAndDeleteShields import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="shields"),
    path('<id>/',PutAndDelete.as_view(), name="shields_detail")
]

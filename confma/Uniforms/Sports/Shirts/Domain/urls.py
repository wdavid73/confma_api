from django.urls import path,include

from ..Application.GetAndPostShirtsSports import GetAndPost
from ..Application.PutAnddeleteShirtsSport import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_shirts_sports"),
    path('<id>/', PutAndDelete.as_view(), name="shirst_sport_detail")
]
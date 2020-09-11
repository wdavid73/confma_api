from django.urls import path,include

from ..Application.GetAndPostShirtsMale import GetAndPost
from ..Application.PutAndDeleteShirtsMale import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="get_shirts_male"),
    path('<id>/', PutAndDelete.as_view(), name="shirts_male_detail")
]
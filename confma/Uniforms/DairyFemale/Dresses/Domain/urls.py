from django.urls import path, include

from ..Application.GetAndPostDresses import GetAndPost
from ..Application.PutAndDeleteDresses import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="dresses"),
    path('<id>/', PutAndDelete.as_view(), name="dresses_details")
]

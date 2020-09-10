from django.urls import path, include

from ..Application.GetAndPostDresses import GetAndPostDress
from ..Application.PutAndDeleteDresses import PutAndDeleteDresses

urlpatterns = [
    path('', GetAndPostDress.as_view(), name="dresses"),
    path('<id>/' ,PutAndDeleteDresses.as_view(), name="dresses_details" )
]

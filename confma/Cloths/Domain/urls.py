from django.urls import path

from ..Application.DeleteCloth import delete_log
from ..Application.GetAndPostCloth import GetAndPost
from ..Application.PutAndDeleteCloth import PutAndDelete

urlpatterns = [
    path('', GetAndPost.as_view(), name="cloth"),
    path('delete/<int:_id>/', delete_log, name='cloth_delete'),
    path('<id>/', PutAndDelete.as_view(),name="cloth_detail"),
]

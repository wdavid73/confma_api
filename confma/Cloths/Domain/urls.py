from django.urls import path

from ..Application.GetAndPostCloth import GetAndPostCloth
from ..Application.PutAndDeleteCloth import PutAndDeleteCloth
from ..Application.DeleteCloth import delete_log

urlpatterns = [
    path('', GetAndPostCloth.as_view(), name="cloth"),
    path('<id>/', PutAndDeleteCloth.as_view(),
         name="cloth_detail"),
    path('delete/<int:_id>/', delete_log, name='cloth_delete'),
]

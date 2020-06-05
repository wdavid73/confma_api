from django.urls import path

from ..Application.DeleteClient import delete_log
from ..Application.GetAndPostClient import GetAndPostClient
from ..Application.PutAndDeleteClient import PutAndDeleteClient

urlpatterns = [
    path('', GetAndPostClient.as_view(), name="client_get"),
    path('<id>/', PutAndDeleteClient.as_view(), name="client_put"),
    path('delete/<int:_id>/', delete_log, name='client_delete_log'),
]

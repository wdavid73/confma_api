from django.urls import path

from ..Application.DeleteClient import delete_log
from ..Application.GetAndPostClient import GetAndPostClient
from ..Application.PutAndDeleteClient import PutAndDeleteClient
from ..Application.DetailOneClient import DetailOneClient
from ..Application.FindClient import FindClient

urlpatterns = [
    path('', GetAndPostClient.as_view(), name="client_get"),
    path('find/<id>/', FindClient.as_view(), name="find_client"),
    path('details/<id>/', DetailOneClient.as_view(), name="details_client"),
    path('delete/<int:_id>/', delete_log, name='client_delete_log'),
    path('<id>/', PutAndDeleteClient.as_view(), name="client_put"),
]

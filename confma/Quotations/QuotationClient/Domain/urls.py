from django.urls import path

from ..Application.ClientNotDuplicated import ClientNotDuplicatedInQuotation
from ..Application.Delete import delete_log
from ..Application.GetAndPost import GetAndPostQuotationClient
from ..Application.PutAndDelete import PutAndDeleteQuotationClient

urlpatterns = [
    path('', GetAndPostQuotationClient.as_view(), name="quotation_client"),
    path('<id>/', PutAndDeleteQuotationClient.as_view(),name="quotation_client_detail"),
    path('delete/<int:_id>/', delete_log, name='qc_delete'),
    path('client_valid/<int:_id>/', ClientNotDuplicatedInQuotation,name='client_id'),
]

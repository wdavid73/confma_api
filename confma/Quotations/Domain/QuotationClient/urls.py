from django.urls import path

from ...Application.QuotationClient.ClientNotDuplicated import \
    ClientNotDuplicatedInQuotation
from ...Application.QuotationClient.Delete import delete_log
from ...Application.QuotationClient.GetAndPost import \
    GetAndPostQuotationClient
from ...Application.QuotationClient.PutAndDelete import \
    PutAndDeleteQuotationClient

urlpatterns = [
    path('', GetAndPostQuotationClient.as_view(),name="quotation_client"),
    path('<id>/',PutAndDeleteQuotationClient.as_view(),name="quotation_client_detail"),
    path('delete/<int:_id>/',delete_log, name='qc_delete'),
    path('clientnotduplicated/<int:_id>/',ClientNotDuplicatedInQuotation,name='qc_client_not_duplicated'),
]

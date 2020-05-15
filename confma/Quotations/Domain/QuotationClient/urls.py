from django.urls import path

from ...Application.QuotationClient.GetAndPost import \
    GetAndPostQuotationClient
from ...Application.QuotationClient.PutAndDelete import \
    PutAndDeleteQuotationClient
from ...Application.QuotationClient.Delete import delete_log
from ...Application.QuotationClient.ClientNotDuplicated import \
    ClientNotDuplicatedInQuotation

urlpatterns = [
    path('quotations_clients/', GetAndPostQuotationClient.as_view(),
         name="quotation_client"),
    path('quotations_clients/<id>/',
         PutAndDeleteQuotationClient.as_view(),
         name="quotation_client_detail"),
    path('quotations_clients/delete/<int:_id>/',
         delete_log, name='qc_delete'),
    path('quotations_clients/clientnotduplicated/<int:_id>/',
         ClientNotDuplicatedInQuotation,
         name='qc_client_not_duplicated'),
]

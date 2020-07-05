from django.urls import path

from ..Application.ClothWithOutQuotation import ClothWithOutQuotation
from ..Application.DeleteQuotation import delete_log
from ..Application.GetAndPostQuotation import GetAndPost
from ..Application.PutAntDelete import PutAndDelete
from ..Application.quotation import isValidCloth

urlpatterns = [
    path('quotations/', GetAndPost.as_view(), name="quotation"),
    path('quotations/<id>/', PutAndDelete.as_view(),name="quotation_detail"),
    path('quotations/delete/<int:_id>/', delete_log,name='quotation_delete'),
    path('quotations_cloth/', ClothWithOutQuotation,name='cloth_without_quotation'),
    path('isvalidcloth/<int:id>/', isValidCloth,name="is_valid_cloth"),
]

from django.urls import path

from ..Application.ClothWithOutQuotation import ClothWithOutQuotation
from ..Application.DeleteQuotation import delete_log
from ..Application.GetAndPostQuotation import GetAndPost
from ..Application.PutAntDelete import PutAndDelete
from ..Application.isValidCloth import isValidCloth
from ..Application.GetOneQuotation import GetOneQuotation

urlpatterns = [
    path('', GetAndPost.as_view(), name="quotation"),
    path('quotations_cloth/', ClothWithOutQuotation,
         name='cloth_without_quotation'),
    path('delete/<int:_id>/', delete_log, name='quotation_delete'),
    path('isvalidcloth/<int:id>/', isValidCloth.as_view(),
         name="is_valid_cloth"),
    path('get_one/<int:_id>/', GetOneQuotation, name='quotation_get_one'),
    path('<id>/', PutAndDelete.as_view(), name="quotation_detail"),
]

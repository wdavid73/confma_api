from django.urls import path

from ..Application.DeleteRental import delete_log
from ..Application.GetAndPostRental import GetAndPost
from ..Application.PutAndDeleteRental import PutAndDelete
from ..Application.RefundRental import RefundRental
from ..Application.rental import ClothWithOutRental

urlpatterns = [
    path('', GetAndPost.as_view(), name="rental"),
    path('cloths/', ClothWithOutRental, name="cloth_without_rental"),
    path('<id>/', PutAndDelete.as_view(), name="rental_detail"),
    path('delete/<int:_id>/', delete_log, name='rental_delete'),
    path('refund/<int:_id>/', RefundRental, name='rental_refund'),

]

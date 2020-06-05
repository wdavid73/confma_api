from django.urls import path

from ..Application.DeleteRental import delete_log
from ..Application.GetAndPostRental import GetAndPostRental
from ..Application.PutAndDeleteRental import PutAndDeleteRental
from ..Application.RefundRental import RefundRental
from ..Application.rental import ClothWithOutRental

urlpatterns = [
    path('', GetAndPostRental.as_view(), name="rental"),
    path('<id>/', PutAndDeleteRental.as_view(),
         name="rental_detail"),
    path('delete/<int:_id>/', delete_log,
         name='rental_delete'),
    path('refund/<int:_id>/', RefundRental,
         name='rental_refund'),
    path('rentals_cloth/', ClothWithOutRental,
         name="cloth_without_rental"),
]

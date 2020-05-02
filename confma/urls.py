from django.urls import path, include
from rest_framework import routers

from . import views2
from .views import client, cloth, rental, quotation, quotation_client
from .views.client import ClientViews, ClientDetailView
from .views.cloth import ClothView, ClothDetailView
from .views.quotation import QuotationDetailView, QuotationView
from .views.quotation_client import QuotationClientView, QuotationClientDetailView
from .views.rental import RentalDetailView, RentalView

app_name = 'confma'

urlpatterns = [

    path('clients/', ClientViews.as_view(), name="client"),
    path('clients/<id>/', ClientDetailView.as_view(), name="client_detail"),
    path('clients/delete/<int:_id>/', client.delete_log, name='client_delete'),
    path('clients/find/<int:_id>/', client.FindClient, name='client_find'),

    path('cloths/', ClothView.as_view(), name="cloth"),
    path('cloths/<id>/', ClothDetailView.as_view(), name="cloth_detail"),
    path('cloths/delete/<int:_id>/', cloth.delete_log, name='cloth_delete'),
    path('cloths/details/<int:_id>/', cloth.DetailsCloth, name='cloth_with_details'),

    path('rentals/', RentalView.as_view(), name="rental"),
    path('rentals/<id>/', RentalDetailView.as_view(), name="rental_detail"),
    path('rentals/delete/<int:_id>/', rental.delete_log, name='rental_delete'),
    path('rentals/refund/<int:_id>/', rental.RefundRental, name='rental_refund'),
    path('rentals_cloth/', rental.ClothWithOutRental, name="cloth_without_rental"),

    

    path('quotations/', QuotationView.as_view(), name="quotation"),
    path('quotations/<id>/', QuotationDetailView.as_view(), name="quotation_detail"),
    path('quotations/delete/<int:_id>/', quotation.delete_log, name='quotation_delete'),
    path('quotations/find/<str:cloth_name>/', quotation.FindQuotations, name='quotation_find'),
    path('quotations_cloth/' , quotation.ClothWithOutQuotation, name='clothwithoutquotation'),

    path('quotations_clients/', QuotationClientView.as_view(), name="quotation_client"),
    path('quotations_clients/<id>/', QuotationClientDetailView.as_view(), name="quotation_client_detail"),
    path('quotations_clients/delete/<int:_id>/', quotation_client.delete_log, name='qc_delete'),
    path('quotations_clients/clientnotduplicated/<int:_id>/', quotation_client.ClientNotDuplicatedInQuotation, name='qc_client_not_duplicated'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

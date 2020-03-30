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
router = routers.DefaultRouter()
# router.register(r'client', views2.ClientViewSet)
router.register(r'cloth', views2.ClothViewSet)
router.register(r'quotation', views2.QuotationViewSet)
router.register(r'quotation_client', views2.QuotationClientViewSet)
router.register(r'rental', views2.RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('clients/', ClientViews.as_view(), name="client"),
    # path('clients/<int:_id>/', ClientDetailView.as_view(), name="client_detail"),
    path('clients/<id>/', ClientDetailView.as_view(), name="client_detail"),
    path('clients/delete/<int:_id>/', client.delete_log, name='client_delete'),

    path('cloths/', ClothView.as_view(), name="cloth"),
    path('cloths/<id>/', ClothDetailView.as_view(), name="cloth_detail"),
    path('cloths/delete/<int:_id>/', cloth.delete_log, name='client_delete'),

    path('rentals/', RentalView.as_view(), name="rental"),
    path('rentals/<id>/', RentalDetailView.as_view(), name="rental_detail"),
    path('rentals/delete/<int:_id>/', rental.delete_log, name='rental_delete'),

    path('quotations/', QuotationView.as_view(), name="quotation"),
    path('quotations/<id>/', QuotationDetailView.as_view(), name="quotation_detail"),
    path('quotations/delete/<int:_id>/', quotation.delete_log, name='quotation_delete'),

    path('quotations_clients/', QuotationClientView.as_view(), name="quotation_client"),
    path('quotations_clients/<id>/', QuotationClientDetailView.as_view(), name="quotation_client"),
    path('quotations_clients/delete/<int:_id>/', quotation_client.delete_log, name='qc_delete'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# path('snippets/', views.SnippetList.as_view()),
# path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

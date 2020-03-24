from django.urls import path, include
from rest_framework import routers

from . import views2
from .views import client, cloth, rental
from .views.client import ClientViews, ClientDetailView
from .views.cloth import ClothView, ClothDetailView
from .views.rental import RentalDetailView, RentalView

router = routers.DefaultRouter()
router.register(r'client', views2.ClientViewSet)
router.register(r'cloth', views2.ClothViewSet)
router.register(r'quotation', views2.QuotationViewSet)
router.register(r'quotation_client', views2.QuotationClientViewSet)
router.register(r'rental', views2.RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('clients/', ClientViews.as_view(), name="client"),
    path('clients/<int:_id>/', ClientDetailView.as_view(), name="client_detail"),
    path('clients/delete/<int:_id>/', client.delete_log, name='client_delete'),

    path('cloths/', ClothView.as_view(), name="cloth"),
    path('cloths/<int:_id>/', ClothDetailView.as_view(), name="cloth_detail"),
    path('cloths/delete/<int:_id>/', cloth.delete_log, name='client_delete'),

    path('rentals/', RentalView.as_view(), name="rental"),
    path('rentals/<int:_id>/', RentalDetailView.as_view(), name="rental_detail"),
    path('rentals/delete/<int:_id>/', rental.delete_log, name='rental_delete'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# path('snippets/', views.SnippetList.as_view()),
# path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views2
from .views import client

router = routers.DefaultRouter()
router.register(r'client', views2.ClientViewSet)
router.register(r'cloth', views2.ClothViewSet)
router.register(r'quotation', views2.QuotationViewSet)
router.register(r'quotation_client', views2.QuotationClientViewSet)
router.register(r'rental', views2.RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^clients/', client.ClientViews.as_view(), name='client'),
    path('clients_delete/<int:id>/', client.delete_log, name='client_delete'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

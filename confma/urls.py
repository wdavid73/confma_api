from django.urls import path, include
from rest_framework import routers

from . import views2
from .views.client import ClientViews, ClientDetailView, delete_log

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
    path('clients_delete/<int:_id>/', delete_log, name='client_delete'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# path('snippets/', views.SnippetList.as_view()),
# path('snippets/<int:pk>/', views.SnippetDetail.as_view()),

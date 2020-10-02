from django.urls import path, include
from .Common.Application.endpoints import get_endpoints

app_name = 'confma'

urlpatterns = [
    path('', get_endpoints, name='get_endpoints'),
    path('clients/', include('confma.Clients.Domain.urls'), name="clients"),
    path('cloths/', include('confma.Cloths.Domain.urls'), name="cloths"),
    path('rentals/', include('confma.Rentals.Domain.urls'), name="rentals"),
    path('quotations/', include('confma.Quotations.Domain.urls'), name="quotations"),
    path('quotations-clients/', include('confma.Quotations.QuotationClient.Domain.urls'),
         name="quotations-clients"),
    path('uniforms/', include('confma.Uniforms.Domain.urls'), name="uniforms"),
    path('institutions/', include(
        'confma.Institution.Domain.urls'), name="institutions"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

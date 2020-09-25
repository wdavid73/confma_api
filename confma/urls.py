from django.urls import path, include
from .Common.Application.endpoints import get_endpoints
app_name = 'confma'

urlpatterns = [
    path('', get_endpoints, name='get_endpoints'),
    path('clients/', include('confma.Clients.Domain.urls')),
    path('cloths/', include('confma.Cloths.Domain.urls')),
    path('rentals/', include('confma.Rentals.Domain.urls')),
    path('quotations/', include('confma.Quotations.Domain.urls')),
    path('quotations-clients/',
         include('confma.Quotations.QuotationClient.Domain.urls')),
    path('uniforms/', include('confma.Uniforms.Domain.urls')),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework'))

]

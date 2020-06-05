from django.urls import path, include

app_name = 'confma'

urlpatterns = [
    path('clients/', include('confma.Clients.Domain.urls')),
    path('cloths/', include('confma.Cloths.Domain.urls')),
    path('rentals/', include('confma.Rentals.Domain.urls')),
    path('quotations/', include('confma.Quotations.Domain.urls')),
    path('quotations-clients/', include('confma.Quotations.Domain'
                                        '.QuotationClient.urls')),

    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework'))

]

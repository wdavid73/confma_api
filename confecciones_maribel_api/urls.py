from django.contrib import admin
from django.urls import path, include
from .HomePage.index import HomePage

urlpatterns = [
    path('', HomePage),
    path('api/', include('confma.urls', namespace='confma')),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

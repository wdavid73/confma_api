from django.contrib import admin
from django.urls import path, include
from .HomePage.index import HomePage

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePage),
    path('api/', include('confma.urls', namespace='confma')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

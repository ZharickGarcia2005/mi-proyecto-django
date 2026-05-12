from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- Nueva importación
from django.conf.urls.static import static  # <-- Nueva importación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('portfolio/', include('portfolio.urls')),
]

# Permitir que Django muestre las imágenes mientras estamos desarrollando
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
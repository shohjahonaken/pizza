from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from pages.views import home_page_viem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_viem)
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
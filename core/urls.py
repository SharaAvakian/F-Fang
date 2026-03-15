from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Template-rendered pages (HTML frontend)
    path('', include('products.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),

    # REST API endpoints
    path('api/', include('api.urls')),
    path('api/users/', include('users.api_urls')),
    path('api/products/', include('products.api_urls')),
    path('api/orders/', include('orders.api_urls')),
    path('api/cart/', include('cart.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

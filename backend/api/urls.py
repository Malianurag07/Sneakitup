from django.contrib import admin
from django.urls import path, include, re_path  # <-- Added re_path here
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve           # <-- Added serve here

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Cart URLs
    path('cart/', include('cart.urls', namespace='cart')),

    # Customizer URLs
    path('customizer/', include('customizer.urls')),
    
    # Wishlist URLs
    path('wishlist/', include('wishlist.urls')),

    # Product URLs (Homepage)
    path('', include('products.urls', namespace='products')),
]

# Standard Local Development Static Files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 👇 "RESUME MODE" - Force serve static/media files on Render 👇
# This manually handles images even when DEBUG=False on the live server
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
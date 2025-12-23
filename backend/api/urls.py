from django.contrib import admin
from django.urls import path, include

# We do NOT import 'views' here.

# Import these two for media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This line tells Django to look at your 'cart/urls.py' file
    path('cart/', include('cart.urls', namespace='cart')),

    path('customizer/', include('customizer.urls')), # <--- Add this
    
    # This line tells Django to look at your 'products/urls.py' file
    path('', include('products.urls', namespace='products')),
    
    path('wishlist/', include('wishlist.urls')),  # ✅ add this lin
]

# This is also necessary to see your shoe images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


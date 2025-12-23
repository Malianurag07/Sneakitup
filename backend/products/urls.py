from django.urls import path
from . import views

# THIS IS THE FIX:
# We are officially naming this URL configuration 'products'
app_name = 'products'

urlpatterns = [
    # This is your existing homepage
    path('', views.home_page, name='home'),
    
    # This is your existing shop page
    path('shop/', views.shop_page, name='shop'),
    
    # This is your existing detail page URL
    path('shoe/<int:pk>/', views.product_detail_page, name='product_detail'),
]


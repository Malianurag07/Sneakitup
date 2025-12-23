from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.cart_remove, name='cart_remove'),
    path('test_session/', views.test_session),

]

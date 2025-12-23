from django.urls import path
from . import views

app_name = 'customizer'

urlpatterns = [
    path('', views.customize_shoe, name='index'),
]
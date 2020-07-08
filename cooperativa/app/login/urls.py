from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='autenticar'),
    path('salir_sistema', views.salirSistema, name='salir_sistema'),
]
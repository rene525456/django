from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='clientes'),
    path('nuevo/', views.crear, name='crear_cliente'),
    path('modificar/', views.modificar, name='modificar_cliente'),
]

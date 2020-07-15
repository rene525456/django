from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='transacciones'),
    path('deposito/<str:cedula>/<str:numero>/', views.transaccionDeposito, name='deposito'),
]
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns=[
    path('', views.listaCliente.as_view()),
    path('cedula', views.cedula.as_view()),
    path('apellido', views.apellido.as_view()),
    path('genero', views.genero.as_view()),

]

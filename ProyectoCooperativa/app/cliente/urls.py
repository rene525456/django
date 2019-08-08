from django.urls import path

from . import views

urlpatterns=[
    path('', views.principal, name='clientes'),
    path('primerMensaje/', views.saludar),
    path('crear/', views.crear, name='crear'),
    path('crearCuenta/', views.crearCuenta, name='cuenta'),
    path('modificar/', views.modificar),
    path('eliminar/', views.eliminar),
    path('baja/', views.baja),
    path(r'^transaccionDeposito/(?P<cedula>\d+)(?P<numero>d+)/$', views.transaccionDeposito, name='deposito'),
    path(r'^transaccionRetiro/(?P<cedula>\d+)(?P<numero>d+)/$', views.transaccionRetiro, name='retiro'),
    path('listar/', views.listar, name='listar'),
    path('transferenciaLista/',views.transferenciaLista,name='transferenciaLista'),
    path('transferencia/',views.transferencia,name='transferencia'),
    path('buscarTransferencia/',views.buscarTransferencia,name='buscarTransferencia'),
    path('Reporte/',views.reporte,name='reporte'),



]

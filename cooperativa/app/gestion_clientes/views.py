from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from app.modelo.models import Cliente, Cuenta
from .forms import ClienteFormulario, CuentaFormulario
from django.contrib.auth.models import User, Group

@login_required
def index(request):
    usuario = request.user
    #grupos = User.objects.filter(username=usuario.username)[0].groups.all()
    grupos = [ x.name for x in usuario.groups.all()]
    if usuario.groups.filter(name = 'administrativos').exists():
        listaCliente = Cliente.objects.all().order_by('apellidos')
        return render(request,'clientes/principal.html', locals())
    else:
        return render(request,'login/aceso_prohibido.html', locals())

def crear(request):
    formulario_cliente = ClienteFormulario(request.POST)
    formulario_cuenta = CuentaFormulario(request.POST)
    if request.method == 'POST':
        if formulario_cliente.is_valid() and formulario_cuenta.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.genero = datos_cliente.get('genero')
            cliente.estadoCivil = datos_cliente.get('estadoCivil')
            cliente.correo = datos_cliente.get('correo')
            cliente.telefono = datos_cliente.get('telefono')
            cliente.celular = datos_cliente.get('celular')
            cliente.direccion = datos_cliente.get('direccion')
            cliente.save()
            cuenta = Cuenta()
            datos_cuenta = formulario_cuenta.cleaned_data
            cuenta.numero = datos_cuenta.get('numero')
            cuenta.saldo = datos_cuenta.get('saldo')
            cuenta.tipoCuenta = datos_cuenta.get('tipoCuenta')
            cuenta.cliente = cliente
            cuenta.save()
            return redirect(index)
    return render(request, 'clientes/formulario_crear.html', locals())


def modificar(self):
    return HttpResponse('modificar cliente')

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from app.modelo.models import Cliente, Cuenta, Transaccion
from .forms import FormularioTransaccion

@login_required
def index(request):
    usuario = request.user
    grupos = [ x.name for x in usuario.groups.all()]
    cliente = None
    cuentas = None
    if usuario.groups.filter(name  = 'cajeros').exists():
        queryset = request.GET.get("cedula")
        print(queryset)
        if queryset:
            cliente = Cliente.objects.get(cedula=queryset)
            print(cliente)
            cuentas = Cuenta.objects.filter(cliente = cliente.cliente_id)
            print(cuentas)
        return render (request,'transacciones/principal.html',{'cliente':cliente, 'cuentas': cuentas, 'grupos':grupos})
    else:
        return render (request,'login/acceso_prohibido.html',locals())

def transaccionDeposito(request, cedula, numero):
    usuario = request.user
    grupos = [ x.name for x in usuario.groups.all()]
    if usuario.groups.filter(name  = 'cajeros').exists():
        formulario = FormularioTransaccion(request.POST)
        cliente = Cliente.objects.get(cedula=cedula)
        cuenta = Cuenta.objects.get(numero=numero)
        if request.method == 'POST':
            if formulario.is_valid():
                datos = formulario.cleaned_data
                transaccion = Transaccion()
                transaccion.tipo = 'deposito'
                transaccion.valor = float(datos.get('valor'))
                transaccion.descripcion = datos.get('descripcion')
                transaccion.responsable = usuario.username
                transaccion.cuenta = cuenta
                transaccion.save()
                valorDeposito = float(datos.get('valor')) + float(cuenta.saldo) #cambia el valor de cadenas a double
                cuenta.saldo = valorDeposito
                cuenta.save()
                return HttpResponse('Transacción exitosa') 
        else:
            return render(request, 'transacciones/transaccionDeposito.html', locals())
    else:
        return render (request,'login/acceso_prohibido.html',locals())

    #return HttpResponse('soy el depósito')

    """
    fecha = models.DateTimeField(auto_now_add = True, null = False)

"""
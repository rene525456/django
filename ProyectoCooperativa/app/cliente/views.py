from django.shortcuts import render, redirect

from .forms  import FormularioCliente, FormularioCuenta, FormularioTransaccion

from django.http import HttpResponse
from app.modelo.models import Cliente, Cuenta, Transaccion
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template,render_to_string

import io
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration
from django.template.loader import get_template,render_to_string
from django.http import FileResponse
from reportlab.pdfgen import canvas

@login_required
def principal(request):
    usuario=request.user
    print('xxxxxxxxxxxx')
    print(usuario)
    if usuario.has_perm('modelo.add_cliente'):
        print('tienen el permiso')
        listaClientes= Cliente.objects.all().filter(estado=True).order_by('apellidos')
        listaCuenta= Cuenta.objects.all().filter(estado=True).order_by('numero')
        listaT=Cuenta.objects.all().filter().values('numero', 'transaccion__fecha', 'transaccion__tipo', 'transaccion__valor', 'transaccion__responsable').order_by('transaccion__fecha')
        context={
            'lista':listaClientes,
            'listaC':listaCuenta,
            'listaTransaccion':listaT,
        }
        return render(request, 'cliente/principal_cliente.html', context)
    else:
        return render(request, 'login/acceso_prohibido.html')

@login_required
def listar(request):
    usuario=request.user
    print('xxxxxxxxxx')
    print(usuario)
    if usuario.has_perm('modelo.add_cliente'):
        print('tiene el permiso')
        listaC=Cliente.objects.all().filter().values('cedula', 'nombres', 'apellidos', 'correo','direccion', 'cuenta__numero', 'cuenta__saldo', 'cuenta__tipoCuenta').order_by('apellidos')
        context={
            'listaCuentas': listaC,
        }
        return render(request, 'cuenta/listar.html', context)
    else:
        return render(request, 'login/acceso_prohibido.html')

#user=request.user
#user.get_all_permissions()
#user.get_group_permissions()
#user.has_perms()
#user.has_perm()
#user.user_permissions.remove()
#user.is_member()
#------------------------------------

def saludar(request):
    return HttpResponse('Hola Clase')

@login_required
def crear(request):
    usuario=request.user
    formulario = FormularioCliente(request.POST)
    formulario2= FormularioCuenta (request.POST)
    if request.method == 'POST':
        if formulario.is_valid() and formulario2.is_valid():
            if usuario.groups.filter(name='Cajeros').exists():
                datos = formulario.cleaned_data
                cliente = Cliente()
                cuenta=Cuenta()
                cliente.cedula = datos.get('cedula')
                cliente.apellidos = datos.get('apellidos')
                cliente.nombres = datos.get('nombres')
                cliente.genero = datos.get('genero')
                cliente.estadoCivil=datos.get('estadoCivil')
                cliente.fechaNacimiento=datos.get('fechaNacimiento')
                cliente.correo=datos.get('correo')
                cliente.telefono=datos.get('telefono')
                cliente.celular=datos.get('celular')
                cliente.direccion=datos.get('direccion')
                cliente.save()
                datos2 = formulario2.cleaned_data
                cuenta.numero=datos2.get('numero')
                cuenta.estado=datos2.get('estado')
                cuenta.saldo=datos2.get('saldo')
                cuenta.tipoCuenta=datos2.get('tipoCuenta')
                cuenta.cliente=cliente
                cuenta.save()
                return redirect(principal)
            else:
                return render(request, 'login/acceso_prohibido.html')

    return render(request, 'cliente/crear_cliente.html', locals())


@login_required
def crearCuenta(request):
    usuario=request.user
    dni= request.GET['cedula']
    cliente= Cliente.objects.get(cedula=dni)
    formulario2= FormularioCuenta(request.POST)
    if request.method == 'POST':
        if formulario2.is_valid():
            if usuario.groups.filter(name='Cajeros').exists():
                datos2 = formulario2.cleaned_data
                cuenta=Cuenta()
                cuenta.numero=datos2.get('numero')
                cuenta.estado=datos2.get('estado')
                cuenta.saldo=datos2.get('saldo')
                cuenta.tipoCuenta=datos2.get('tipoCuenta')
                cuenta.cliente=Cliente.objects.get(cedula=dni)
                cuenta.save()
                return redirect(principal)
            else:
                return render(request, 'login/acceso_prohibido.html')

    return render(request, 'cuenta/crear_cuenta.html', locals())


@login_required
def modificar(request):
    usuario=request.user
    if usuario.groups.filter(name='Gerentes').exists():
        dni= request.GET['cedula']
        cliente= Cliente.objects.get(cedula=dni)
        if request.method=='POST':
            formulario= FormularioCliente(request.POST)
            if formulario.is_valid():
                datos=formulario.cleaned_data
                cliente.cedula=datos.get('cedula')
                cliente.nombres=datos.get('nombres')
                cliente.apellidos=datos.get('apellidos')
                cliente.genero=datos.get('genero')
                cliente.estadoCivil=datos.get('estadoCivil')
                cliente.fechaNacimiento=datos.get('fechaNacimiento')
                cliente.correo=datos.get('correo')
                cliente.telefono=datos.get('telefono')
                cliente.celular=datos.get('celular')
                cliente.direccion=datos.get('direccion')
                cliente.save()
                return redirect(principal)
        else:
            formulario= FormularioCliente(instance=cliente)
            context={
                'f': formulario,
                'mensaje':'Bienvenidos',
            }
        return render(request, 'cliente/modificar.html', context)

    else:
        return render(request, ('login/acceso_prohibido.html'))


@login_required
def eliminar(request):
    usuario=request.user
    if usuario.groups.filter(name='Gerentes').exists():
        dni= request.GET['cedula']
        cliente= Cliente.objects.get(cedula=dni)
        cliente.estado=False
        cliente.save()
        return redirect(principal)
    else:
        return render(request, ('login/acceso_prohibido.html'))


@login_required
def baja(request):
    usuario=request.user
    if usuario.groups.filter(name='Gerentes').exists():
        num= request.GET['numero']
        cuenta= Cuenta.objects.get(numero=num)
        cuenta.estado=False
        cuenta.save()
        return redirect(principal)
    else:
        return render(request, ('login/acceso_prohibido.html'))

    
@login_required
def transaccionDeposito(request, cedula, numero):
    usuario=request.user
    if usuario.groups.filter(name='Cajeros').exists():
        formularioTransaccion= FormularioTransaccion(request.POST)
        cliente=Cliente.objects.all().filter(cedula=cedula)
        cuenta=Cuenta.objects.all().filter(numero=numero)
        if request.method=='POST':
            if formularioTransaccion.is_valid():
                datosTransaccion=formularioTransaccion.cleaned_data
                transaccion = Transaccion()
                transaccion.tipo= 'deposito'
                deposito=float(datosTransaccion.get('valor'))
                num=str(Cuenta.objects.get(numero=numero))
                num=num.split(';')
                actualSaldo=float(num[0])
                cedulaRemitente=cedula
                numeroRemitente=numero
                monto=datosTransaccion.get('valor')
                tipo='deposito'
                transaccion.valor=datosTransaccion.get('valor')
                transaccion.descripcion=datosTransaccion.get('descripcion')
                transaccion.responsable=datosTransaccion.get('responsable')
                transaccion.cuenta=Cuenta.objects.get(cuenta_id=int(num[1]))
                transaccion.save()
                for c in cuenta:
                    c.saldo=round(actualSaldo+deposito, 3)
                    c.save()
                    mensaje="Transaccion exitosa"
                    valor=True;
                return render (request,'cuenta/estatus.html',locals())
        else:
            return render(request, 'cuenta/transaccionDeposito.html', locals())
    else:
        return render(request, ('login/acceso_prohibido.html'))





@login_required
def transaccionRetiro(request, cedula, numero):
    usuario=request.user
    if usuario.groups.filter(name='Cajeros').exists():
        formularioTransaccion= FormularioTransaccion(request.POST)
        cliente=Cliente.objects.all().filter(cedula=cedula)
        cuenta=Cuenta.objects.all().filter(numero=numero)
        if request.method=='POST':
            if formularioTransaccion.is_valid():
                datosTransaccion=formularioTransaccion.cleaned_data
                transaccion = Transaccion()
                transaccion.tipo= 'retiro'
                deposito=float(datosTransaccion.get('valor'))
                num=str(Cuenta.objects.get(numero=numero))
                num=num.split(';')
                actualSaldo=float(num[0])
                cedulaRemitente=cedula
                numeroRemitente=numero
                monto=datosTransaccion.get('valor')
                tipo='retiro'
                transaccion.valor=datosTransaccion.get('valor')
                transaccion.descripcion=datosTransaccion.get('descripcion')
                transaccion.responsable=datosTransaccion.get('responsable')
                transaccion.cuenta=Cuenta.objects.get(cuenta_id=int(num[1]))
                transaccion.save()
                for c in cuenta:
                    c.saldo=round(actualSaldo-deposito, 3)
                    c.save()
                    mensaje="Transaccion exitosa"
                    valor=True;
                return render (request,'cuenta/estatus.html',locals())
        else:
            return render(request, 'cuenta/transaccionRetiro.html', locals())
    else:
        return render(request, ('login/acceso_prohibido.html'))



@login_required
def buscarTransferencia(request):
        confirmar = False
        numero = request.GET['numero']
        lista= Cliente.objects.all().filter(cuenta__numero=numero).values('cedula','nombres','apellidos','correo','cuenta__numero',
        'cuenta__saldo','cuenta__tipoCuenta').order_by('apellidos')
        listaCuenta= Cuenta.objects.all().filter(numero=numero).values('numero',
        'saldo','tipoCuenta')
        data = ''
        for lst in lista.values():
                presentar =lst['cedula']+";"+lst['nombres']+";"+lst['apellidos']+";"+lst['correo']+";"
        for lst in listaCuenta.values():
                presentar += lst['numero']+";"+str(lst['saldo'])+";"+lst['tipoCuenta']
        return HttpResponse(presentar)

@login_required
def transferenciaLista(request):
    usuario=request.user
    if usuario.groups.filter(name='Cajeros').exists():
        lista= Cliente.objects.all().filter().values('cedula','nombres','apellidos','correo','cuenta__numero', 'cuenta__saldo','cuenta__tipoCuenta').order_by('apellidos')
        return render (request,'cuenta/transferencia.html',locals())
    else:
         return render(request, ('login/acceso_prohibido.html'))


@login_required
def transferencia(request):
    numeroR = request.GET['numeroRemitente']
    numeroD = request.GET['numeroDestinatario']
    cedulaR= request.GET['cedulaRemitente']
    cedulaD = request.GET['cedulaDestinatario']
    valor = request.GET['valor']
    descripcion = request.GET['descripcion']
    responsable = request.GET['responsable']
    clienteR=Cliente.objects.all().filter(cedula = cedulaR)
    clienteD=Cliente.objects.all().filter(cedula = cedulaD)
    cuentaD = Cuenta.objects.all().filter(numero = numeroD)
    cuentaR = Cuenta.objects.all().filter(numero = numeroR)
    if clienteR and cuentaR and clienteD and cuentaD:
        transaccion = Transaccion()
        auxR=str(Cuenta.objects.get(numero = numeroR))
        auxD=str(Cuenta.objects.get(numero = numeroD))
        auxR =  auxR.split(';')
        auxD =  auxD.split(';')
        saldoR = float(auxR[0])
        saldoD = float(auxD[0])
        transaccion.tipo= 'transferencia'
        transaccion.valor = round(float(valor),3)
        transaccion.descripcion = descripcion
        transaccion.responsable = responsable
        transaccion.cuenta = Cuenta.objects.get(cuenta_id=int(auxR[1]))
        saldoTotal = float(valor)
        for r in cuentaR:
            r.saldo =round(saldoR-saldoTotal,3)
            r.save()
        transaccion.save()

        for d in cuentaD:
            d.saldo =round(saldoD+saldoTotal,3)
            d.save()
        mensaje ='La transaccion fue exitosa'
        valor = True
        monto =request.GET['valor']
        numeroRemitente=numeroR
        cedulaRemitente=cedulaR
        tipo='transferencia'
        return render (request,'cuenta/estatus.html',locals())
    else:
        valor = False
        mensaje ='Fallo en la transaccion'
        return render (request,'cuenta/estatus.html',locals())

@login_required
def reporte( request):
    aux1 = request.GET['numeroRemitente']
    aux2= request.GET['cedulaRemitente']
    valor = request.GET['valor']
    tipo=request.GET['tipo']
    user = request.user.username
    cliente= Cliente.objects.all().filter(cedula = aux2 ).values('nombres','apellidos')
    cuenta = Cuenta.objects.all().filter(numero = aux1).values('tipoCuenta')
    vista = render_to_string('./../template/reporteTransacciones.html',locals())
    respuesta = HttpResponse(content_type='application/pdf')
    archivoPDF = HTML(string=vista).write_pdf()
    respuesta = HttpResponse(archivoPDF, content_type='application/pdf')
    respuesta['Content-Disposition'] = 'filename="reporte.pdf"'
    return respuesta
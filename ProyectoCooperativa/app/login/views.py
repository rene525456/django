from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


from .forms import FormularioLogin


# Create your views here.

def loginPage(request):
    if request.method=='POST':
        formulario= FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave= request.POST['password']
            user= authenticate(username=usuario, password=clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('clientes'))
                    #messages.warning(request, 'Te has identificado de forma correcta')
                else:
                    messages.warning(request, 'Usuario inactivo')
            else:
                messages.warning(request, 'Usuario y/o contraseña incorrecta')


    else:
        formulario= FormularioLogin()

    context={
        'f':formulario,
    }
    return render (request, 'login/login.html', context)


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_page'))


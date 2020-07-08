from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import FormularioLogin

def index(request):
    if request.method=='POST':
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username = usuario, password = clave)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #obtener todos los grupos
                    return HttpResponseRedirect(reverse('index'))
                
    else:
        formulario = FormularioLogin()
    contex = {
        'formulario': formulario
    }
    return render(request, 'login/autenticar.html', contex)

def salirSistema(request):
    logout(request)
    return HttpResponseRedirect(reverse('clientes'))
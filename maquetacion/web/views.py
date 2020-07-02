from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"home.html")
    #return HttpResponse('hola soy el home por el momento')

def servicios(request):
    return render(request,"servicios.html")
    #return HttpResponse('hola soy el servico')

def tienda(request):
    return render(request,"tienda.html")
    #return HttpResponse('hola soy la tienda')

def blog(request):
    return render(request,"blog.html")
    #return HttpResponse('hola soy el blog')

def contacto(request):
    return render(request,"contacto.html")
    #return HttpResponse('hola soy el contacto')
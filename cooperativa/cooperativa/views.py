from django.shortcuts import render

def index(request):
    usuario = request.user
    grupos = [x.name for x in usuario.groups.all()]
    return render(request,'index.html', locals())


from django.shortcuts import render

from app.modelo.models import Cliente

from rest_framework.views import APIView

from rest_framework.response import Response

from .serializable import ClienteSerializable
# Create your views here.

class listaCliente(APIView):
    def get(self, request):
        lista= Cliente.objects.all() #lista de objetos normales
        objetoSerializable= ClienteSerializable(lista, many=True)#se envia la lista para transformarlos en objetos serializables
        return Response(objetoSerializable.data)


class cedula(APIView):
    def get(self, request):
        dni=request.GET["cedula"]
        lista= Cliente.objects.all().filter(cedula=dni) #lista de objetos normales
        objetoSerializable= ClienteSerializable(lista, many=True)#se envia la lista para transformarlos en objetos serializables
        return Response(objetoSerializable.data)

class apellido(APIView):
    def get(self, request):
        apellido=request.GET["apellidos"]
        lista= Cliente.objects.all().filter(apellido) #lista de objetos normales
        objetoSerializable= ClienteSerializable(lista, many=True)#se envia la lista para transformarlos en objetos serializables
        return Response(objetoSerializable.data)


class genero(APIView):
    def get(self, request):
        if request.GET["genero"]=='f':
            lista= Cliente.objects.all().filter(genero='f') #lista de objetos normales
            objetoSerializable= ClienteSerializable(lista, many=True)#se envia la lista para transformarlos en objetos serializables
            return Response(objetoSerializable.data)
        if request.GET['genero']=='m':
            lista= Cliente.objects.all().filter(genero='m') #lista de objetos normales
            objetoSerializable= ClienteSerializable(lista, many=True)#se envia la lista para transformarlos en objetos serializables
            return Response(objetoSerializable.data)




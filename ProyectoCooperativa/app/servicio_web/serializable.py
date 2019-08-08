from rest_framework import serializers

#importa el modelo CLIENTE desde la carpeta app, modelo, models
from app.modelo.models import Cliente


class ClienteSerializable(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields=["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]

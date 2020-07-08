from django import forms
from app.modelo.models import Cliente, Cuenta

class ClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["cedula", "nombres", "apellidos", "genero", "estadoCivil", "correo", "telefono", "celular", "direccion"]
        

class CuentaFormulario(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ["numero", "tipoCuenta", "saldo"]

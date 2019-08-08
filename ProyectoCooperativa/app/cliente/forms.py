from django import forms
from app.modelo.models import Cliente, Cuenta, Transaccion

class FormularioCliente(forms.ModelForm):

    class Meta:
        model=Cliente
        fields=["cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
        widgets={
            'fechaNacimiento':forms.DateInput(format='%d-%m-%Y', attrs={'type':'date'}),
        }

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model=Cuenta
        fields=["numero", "tipoCuenta", "estado", "saldo"]


class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model=Transaccion
        fields=["valor", "descripcion", "responsable"]

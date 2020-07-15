from django.db import models

class Cliente(models.Model):
    listaGenero=(
        ('femenino', 'Femenino'),
        ('masculino', 'Masculino'),
    )
    listaEstadoCivil=(
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo'),
    )
    cliente_id = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length=10, null = False, unique = True)
    nombres = models.CharField(max_length=70, null = False)
    apellidos = models.CharField(max_length=70, null = False)
    genero = models.CharField(max_length=15, choices = listaGenero, null = False, default="femenino")
    estadoCivil = models.CharField(max_length=15, choices = listaEstadoCivil,null = False, default="soltero")
    correo = models.EmailField(max_length=100, null = False)
    telefono = models.CharField(max_length=15, null = False)
    celular = models.CharField(max_length=15, null = False)
    direccion = models.TextField(max_length=75, null = False, default = "Dirección")

    def __str__(self):
        return self.cedula

class Cuenta(models.Model):
    listaTipoCuenta = (
        ('ahorros', 'Ahorros'),
        ('corriente', 'Corriente'),
        ('programado', 'Programado'),
    )
    cuenta_id = models.AutoField(primary_key = True)
    numero = models.CharField(max_length = 20, unique = True, null = False)
    fechaApertura = models.DateField(auto_now_add = True, null = False)
    tipoCuenta = models.CharField(max_length = 30, choices = listaTipoCuenta, default = 'ahorros', null = False)
    saldo = models.DecimalField(max_digits = 10,decimal_places = 3, null = False)
    estado = models.BooleanField(default = True)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)

    def __str__(self):
        cadena = str(self.saldo) + ";" + str(self.cuenta_id)
        return cadena

class Transaccion(models.Model):
    listaTipoTransacciones = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
    )

    transaccion_id = models.AutoField(primary_key = True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    tipo = models.CharField(max_length = 30, choices = listaTipoTransacciones, null = False)
    valor = models.DecimalField(max_digits = 10, decimal_places = 3, null = False)
    descripcion = models.TextField(default='descripción de la transacción')
    responsable = models.CharField(max_length = 100, null = False)
    cuenta = models.ForeignKey(Cuenta, on_delete = models.CASCADE)

    #def __str__(self):
    #    return self.transaccion_id

class Banco(models.Model):
    nombre = models.CharField(primary_key=True, max_length=25)
    direccion = models.CharField(max_length=225)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=200)
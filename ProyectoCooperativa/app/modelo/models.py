from django.db import models

class Cliente(models.Model):
    listaGenero=(
        ('f', 'Femenino'),
        ('m', 'Masculino'),
    )

    listaEstadoCivil=(
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo'),
    )

    cliente_id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, null = False)
    nombres = models.CharField(max_length=70, null = False)
    apellidos = models.CharField(max_length=70, null = False)
    genero = models.CharField(max_length=15, choices = listaGenero, null = False, default="femenino")
    estadoCivil = models.CharField(max_length=15, choices = listaEstadoCivil,null = False, default="soltero")
    fechaNacimiento = models.DateField(auto_now = False, auto_now_add = False, null = False)
    correo = models.EmailField(max_length=100, null = False)
    telefono = models.CharField(max_length=15, null = False)
    celular = models.CharField(max_length=15, null = False)
    direccion = models.TextField(max_length=75, null = False)
    estado=models.BooleanField(default=True)
    #uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.cedula

class Banco(models.Model):
    nombre = models.CharField(primary_key=True, max_length=25)
    direccion = models.CharField(max_length=225)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=200)

class Cuenta(models.Model):
    listaTipo = (
        ('corriente', 'Corriente'),
        ('ahorros', 'Ahorro'),
        ('basica', 'Básica'),
        ('nomina', 'Nómina'),
        ('valores', 'Valores'),
        ('juvenil', 'Juvenil'),
        ('programado', 'Ahorro Programado'),
        ('euros', 'Ahorro en Euros'),
    )

    cuenta_id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20, unique=True, null = False)
    estado = models.BooleanField(default=True)
    fechaApertura = models.DateField(auto_now_add = True, null = False)
    
    tipoCuenta = models.CharField(max_length=30, choices = listaTipo, null = False, default="ahorros")
    saldo = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        string=str(self.saldo)+";"+str(self.cuenta_id)
        return string


class Transaccion(models.Model):
    listaTipoT = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
        ('transferencia', 'Transferencia'),
    )

    transaccion_id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    tipo = models.CharField(max_length=30, choices = listaTipoT, null = False)
    valor = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    descripcion = models.TextField(null = False)
    responsable = models.CharField(max_length=160, null = False)
    cuenta = models.ForeignKey(
        'Cuenta',
        on_delete=models.CASCADE,
    )
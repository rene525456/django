# django


[Alt](UC.png)
Instalación de las libreriias para conectar django con mysql

sudo apt-get install python3-dev
sudo apt-get install python3-dev libmysqlclient-dev

pip install mysqlclient



create database bd_cooperativa
use bd_cooperativa
CREATE USER 'cooperativa'@'localhost' IDENTIFIED BY 'cooperativa';
GRANT ALL PRIVILEGES ON bd_cooperativa.* TO 'cooperativa'@'localhost';
FLUSH PRIVILEGES


***
configurar el settings del proyecto en django cara cambiar la bd

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cooperativa_prueba',
        'USER': 'karla',
        'PASSWORD': 'karka',
        'HOST': 'localhost',
        'PORT': '',
    }
}

Problema con librerias en django
pip3 install djangorestframework
pip3 install weasyprint
pip3 install reportlab

Crear un súper usuario de django
python manage.py createsuperuser

En el admin
	* Crear el grupo Cajeros
		* Se agregar los permisos de add cliente, add cuenta, add transaccion
		* Se agregar los permisos de view cliente, view cuenta, view transaccion

Crear un usuario para cajero y asignarle el grupo























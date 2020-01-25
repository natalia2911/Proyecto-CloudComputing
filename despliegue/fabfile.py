from fabric.api import *
from fabric.contrib.console import confirm
from fabric import *

# Definimos una variable de entorno con el host al que nos vamos a conectar
# y el nombre de usuario
env.user = "vagrant"
env.host = ['proyectocc.westus.cloudapp.azure.com']

def Desinstalar():
	#Borramos el codigo antiguo
	run("sudo rm -rf ./Proyecto-CloudComputing")

def Instalar():
	#Instalamos el servicio clonando eliminando el codigo anterior e instalando los requerimientos
	Desinstalar()
	run("git clone https://github.com/natalia2911/Proyecto-CloudComputing.git")
	with cd("Proyecto-CloudComputing"):
		run('pip3 install --user -r requirements.txt')

def Actualizar():
	#Hacemos un pull de proyecto para descargar las actualizaciones, y volvemos a instalar los requerimientos
	with cd("Proyecto-CloudComputing"):
		run('git pull')
		run('pip3 install --user -r requirements.txt')


def Iniciar():
	with cd("Proyecto-CloudComputing/src"):
		run('gunicorn students-rest:app -t 2 -w 10 -b 0.0.0.0:5050')
        	run('gunicorn examns-rest:app -t 2 -w 10 -b 0.0.0.0:8080')

def Parar():
    run("pkill gunicorn")

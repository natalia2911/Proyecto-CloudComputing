# Provisionamiento y despliegue de las máquinas virtuales

Como hemos mencionado antes, para el provisionamiento y despliegue usaremos máquinas virtuales, así como:

* `Ansible` para el aprovisionamiento.
* `Vagrant` para la orquestación de las máquina virtuales.
* `Fabric` para el despliegue.

Hemos realizado dos tipos de despliegue en local, y en remoto con Azure.

## Despliegue en local
---
Para el despliegue local, hemos usado en primer lugar un fichero de Vagrant, localizado en el directorio de provisionamiento [aquí](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/provision/Vagrantfile)

```
Vagrant.configure("2") do |config|

  # Como imagen utilizaremos el box de Ubuntu 16.04 LTS:
  config.vm.box = "bento/ubuntu-16.04"

  # Box que vamos a utilizar en la máquina virtual.
  config.vm.hostname = "proyectocc-local"

  config.vm.network "private_network", ip: "192.168.56.50"

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "workstation.yml"
	end

end
```

* **config.vm.box**: especificamos el sistema que queremos que se instale en nuestra máquina, en este caso utilizaremos el box de Ubuntu 16.04 LTS.
* **config.vm.hostname**: especificamos el nombre del box que va a tener la máquina virtual.
* **config.vm.network "private_network"**: establecemos la ip privada que queremos que tenga nuestra máquina virtual.
* **config.vm.provision :ansible do |ansible:**
Configuración del provisionamiento con ansible, con nuestro fichero de workstation.yml, Durante el vagrant up, nos permite que el fichero workstation.yml nos instale las dependencias que necesita nuestra máquina. En este caso usaremos uno diferente al que usamos en la máquina virtual remota. 

Para el despliegue, solo tenemos que realizar estas acciones:

* vagrant up: para levantar la máquina
* vagrant provision: para aprovisionar la máquina.
`Podemos hacer el despliegue y el aprovisionamiento a la vez con vagrant up --provision`


## Despliegue en Azure (De forma remota)
---

En primer lugar para el despliegue en Azure, tendremos que tener una cuenta con créditos disponibles para poder levantar la máquina, una vez realizado esto nos logueamos.

`az login`

Una vez realizado esto crearemos un grupo de recursos, y crearemos el servicio principal seleccionando la subscripción que tengamos. 

```
1. az ad sp create-for-rbac -n ProyectoCC --role contributor

2. az account set --subscription <ID SUSCRIPCIÓN>
```

Una vez realizado esto por pantalla nos mostrará una información relevante que tendremos que usar luego para el fichero Vagrantfile, como será:

* La Id de la subscripción, la id del cliente, la contraseña y tenantId --> que luego usaremos como variable de entorno en dicho fichero.

---

A continuación vamos a proceder a la creación y despliegue de nuestra máquina virtual y para eso usamos Vagrant con un plugin de Azure para ello.

El fichero de Vagrantfile está localizado [aquí](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Vagrantfile)

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # Box que vamos a utilizar en la máquina virtual.
  config.vm.box = "proyectocc"
  # Le especificamos la clave, para la conexión mediante ssh de la máquina.
	config.ssh.private_key_path = "~/.ssh/id_rsa"

  	# Configuración de la máquina (proveedor) donde vamos a crear el host de la máquina:
	config.vm.provider :azure do |cc, override|

		# Variables de entorno y parámetros, necesarios para crear nuestra máquina con Azure.
	    	cc.tenant_id = ENV['AZURE_TENANT_ID'] # Tenant id
	    	cc.client_id = ENV['AZURE_CLIENT_ID'] #Id del cliente de azure
	    	cc.client_secret = ENV['AZURE_CLIENT_SECRET']  #Contraseña de del cliente de azure
	    	cc.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']  #Subscripción de Azure.

		# Tamaño de los recursos de Azure
		cc.vm_size = "Standard_A0"
		#Abrimos el puerto 80, que es el que vamos a utilizar
		cc.tcp_endpoints = "80"
		#Nombre de la máquina virtual
		cc.vm_name = "proyectocc"
		#Especificamos la imagen que vamos a montar en nuestra máquina
		cc.vm_image_urn = 'Canonical:UbuntuServer:16.04-LTS:latest'
		#Grupo de recursos en los que se creará la máquina.
		cc.resource_group_name = 'ProyectoCC'
	  end

  # Configuración del provisionamiento con ansible, con nuestro fichero de playbook.yml
  # Durante el vagrant up, nos permite que el fichero playbook.yml nos instale las dependencias que necesita
  # nuestra máquina
	config.vm.provision :ansible do |ansible|
		ansible.playbook = "./provision/playbook.yml"
	end
end
```
* **config.vm.box** : que nos especifica el box que vamos a utilizar en la máquina virtual; tendremos que elegir uno predefinido o crear uno. En nuestro caso usaremos uno predefinido.

`vagrant box add proyectocc https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
`
* **config.ssh.private_key_path**: especificamos la clave para la conexión mediante ssh de la máquina.

* **config.vm.provider :azure do |cc, override|** aquí es donde vamos a proceder a indicar la configuración de la máquina, en el que indicaremos las variables de entorno mencionadas anteriormente, el tamaño del grupo de recursos, el nombre del mismo, el puerto que vamos a usar, y la imagen que queremos montar en nuestra máquina virtual, en este caso es UbuntuServer:16.04

* **config.vm.provision :ansible do |ansible|:** Configuración del provisionamiento con ansible. 

Iniciamos la máquina virtual con `vagrant up -provider=azure`

![MV](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/MVAZURE.png)

![Recursos](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/recursos.png)

---

Para el provisionamiento con ansible hemos utilizado el fichero [playbook.yml](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/provision/playbook.yml)

En este paso se ejecutará el fichero de provisionamiento, pero antes deberemos añadir nuestro host en el fichero : `/etc/ansible/hosts`

Nuestro fichero de provisionamiento: actualiza, instala python, pip, git y descarga el proyecto de la plataforma de github.

```
- hosts: all
  remote_user: vagrant
  become: yes

  tasks:

  - name: Actualizar sistema
    command: apt update

  - name: Instalar Python
    apt:
      pkg: ["python3","python3-pip"]
      state: present

  - name: Instalar Git
    command: apt-get install git

  - name: Descargar proyecto
    git:
      repo: https://github.com/natalia2911/Proyecto-CloudComputing.git
      dest: /Proyecto-CloudComputing
      version: master



```

---
Para el despligue usamos Fabric, con el fichero [Fabfile](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/despliegue/fabfile.py)

```
from fabric.api import *
from fabric.contrib.console import confirm
from fabric import *

# Definimos una variable de entorno con el host al que nos vamos a conectar
# y el nombre de usuario
env.user = "vagrant"
env.host = ['proyectocc.westus.cloudapp.azure.com']

def Desinstalar():
	#Borramos el código antiguo
	run("sudo rm -rf ./Proyecto-CloudComputing")

def Instalar():
	#Instalamos el servicio clonando eliminando el código anterior e instalando los requerimientos
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
```

Las acciones que realizamos para el despliegue son:

* Desinstalar, Instalar, Iniciar los microservicios mediante gunicorn, y también podemos pararlo.

Para probar las funciones del despliegue.

`fab -f despliegue/fabfile.py -H vagrant@104.42.214.221 <Una de las funciones descritas>`

## Medición de prestaciones

Hemos medido tanto las prestaciones de la máquina local, y la remota, y es evidente que de forma remota las prestaciones son muy bajas, mientras que en la máquina local, son aceptables, pero no tan buenas como pudimos ver en hitos anteriores que llegamos a unas 1273.18Hits/segundo.

Como podemos ver en las imágenes, en primer lugar tenemos las prestaciones que se ejecutan de forma remota, 50.25Hits/segundo, prestaciones que no son aceptables, pero las cuales hemos mejorado con la versión en local con 435.29Hits/segundo, de las cuales podemos decir que no son del todo muy buenas, pero que aún así podemos considerarlas como aceptables.


![Remoto](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/prestaciones-remoto.png)

![Local](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/prestaciones-local.png)


## Referencias
* https://blog.deiser.com/es/primeros-pasos-con-ansible
* https://stackoverrun.com/es/q/7574013
* https://www.rubydoc.info/gems/vagrant-azure/1.3.0
* http://www.fabfile.org/
* https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments
* https://vsupalov.com/fabric-2-example-fabfile/
* https://hub.packtpub.com/how-write-your-first-fabfile/
* https://docs.ansible.com/ansible/latest/user_guide/playbooks.html
* https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html
* https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html
*

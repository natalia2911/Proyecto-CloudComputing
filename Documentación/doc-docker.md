# Despliegue con Docker
Usamos docker ya que nos sirve para crear contenedores de forma ligera, y portables de tal forma que nuestro  microservicio puede ejecutarse en cualquier máquina con Docker instalado, independientemente del sistema operativo que la máquina tenga por debajo.

## Instalación:

* Tenemos que configurar el repositorio donde va a estar Docker, en este caso el repositorio de nuestro proyecto. `sudo apt-get update`
* Instalamos todo lo necesario: 
    ```
    - sudo apt-get install apt-transport-https

    - sudo apt-get install ca-certificates

    # Agrega la clave GPG para el repositorio oficial de Docker.

    - sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

    -sudo apt-get install -y docker-ce

    # Comprobamos el estado del servicio:

    -sudo systemctl status docker

    ``` 

    ## Creación Dockerfile

    [Enlace al Dockerfile](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Dockerfile)

    ``` 
    # Seleccionamos la imagen base de alpine, el motivo de la elección ha sido que este sistema ya tiene instalado por defe
    # la versión de python que nosotros usaremos en nuestro proyecto, y también que la imagen que genera este sistema es pequeña.
    FROM python:3.6.8-alpine

    # En la etiqueta LABEL, mostraremos la información del desarrollador, y el email para el contacto
    LABEL NataliaMartir <nataliamartir@correo.ugr.es>

    # Establecemos con la etiqueta WORKDIR cual va a ser el directorio de trabajo
    WORKDIR /src/

    # Copiamos en la imagen todos los archivos necesarios para usar nuestra api rest.
    COPY src/ src/ ./

    #Con el comando run queremos instalar lo necesario para que se pueda crear el contenedor instalamos gunicorn y actualizar pip

    RUN apk add py3-setuptools \
        && pip install --no-cache-dir --upgrade pip \ 
        && pip install --no-cache-dir gunicorn


    #Definimos el puerto donde el contenedor va a escuchar
    #Usamos el puerto 80, ya que es el puerto del protocolo http por defecto.
    # Fuente: https://lemoncode.net/lemoncode-blog/2019/11/5/hola-docker
    EXPOSE 80

    #Ejecutamos gunicorn:
    # Para acceder a la api rest, tendremos que introducirnos en la carpeta src.
    # Usamos --bind para especificar el socket donde va a escuchar, en este caso en el localhost, en el puerto 80.
    CMD cd src && gunicorn students-rest:app --bind 0.0.0.0:80``` 


Vamos a explicar cada uno de los elementos usados:

* **FROM**: indica la imagen que vamos a usar en nuestro contenedor, en este caso hemos elegido la de Python en la versión 3.6.8 que es la que testea nuestro proyecto, con alpine, ya que es un sistema muy liguero y genera unas imagenes muy pequeñas.
* **LABEL**: Mostramos la información del desarrollador, tanto el nombre como un correo de conctato.
* **COPY**: Se copia lo necesario para que funcione la aplicación
* **RUN**: Instalamos lo que necesita nuestra aplicación para funcionar.
* **EXPOSE**: Definimos el puerto donde va a escuchar el contenedor, en este caso es el puerto 80, que por defecto es el puerto del protocolo HTTP, en este caso no lo hemos introducido en una variable de entorno debido a que este puerto es un puerto común y por defecto, pero si que podríamos introducirlo en una variable de entorno.
* **CMD**: Ejecutamos gunicorn, para que arranque la api, Para acceder a la api rest, tendremos que introducirnos en la carpeta src. Usamos --bind para especificar el socket donde va a escuchar, en este caso en el localhost, en el puerto 80.

Para construir la imagen:

` docker build -t natalia2911/proyecto-cloudcomputing .
` 

Ponemos el punto al final, para que nos busque en el directorio donde esta el fichero *Dockerfile* 

# DockerHub

Hemos creado la imagen en DockerHub.

![img](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/dockerhub.png)

Imagen del contenedor: https://hub.docker.com/r/natalia2911/proyecto-cloudcomputing 

Para crear la imagen, hemos entrado a la página  https://hub.docker.com/, y dentro de la parte *Create* hemos elegido *Create Automatic Build* en el repositorio del proyecto.
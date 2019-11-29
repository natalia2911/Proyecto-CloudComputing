# Seleccionamos la imagen base de alpine, el motivo de la elección ha sido que este sistema ya tiene instalado por defe
# la versión de python que nosotros usaremos en nuestro proyecto, y también que la imagen que genera este sistema es pequeña.
FROM python:3.6.8-alpine

# En la etiqueta LABEL, mostraremos la información del desarrollador, y el email para el contacto
LABEL NataliaMartir <nataliamartir@correo.ugr.es>

# Establecemos con la etiqueta WORKDIR cual va a ser el directorio de trabajo
WORKDIR /src/

# Copiamos en la imagen todos los archivos necesarios para usar nuestra api rest.
COPY . ./

#Con el comando run queremos instalar lo necesario para que se pueda crear el contenedor podríamos solo instalar gunicorn y actualizar pip, pero por funcionalidad 
# preferimos que nuestro contenedor instale todos los requirements.
#RUN pip install --upgrade pip && pip install --no-cache-dir -r gunicorn 
RUN pip install --no-cache-dir -r requirements.txt

#Definimos el puerto donde el contenedor va a escuchar
#Usamos el puerto 80, ya que es el puerto del protocolo http por defecto.
# Fuente: https://lemoncode.net/lemoncode-blog/2019/11/5/hola-docker
EXPOSE 80

#Ejecutamos gunicorn:
# Para acceder a la api rest, tendremos que introducirnos en la carpeta src.
# Usamos --bind para especificar el socket donde va a escuchar, en este caso en el localhost, en el puerto 80.
CMD cd src && gunicorn students-rest:app --bind 0.0.0.0:80
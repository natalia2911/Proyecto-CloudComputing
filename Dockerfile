# Seleccionamos la imagen base de alpine, el motivo de la elección ha sido que este sistema ya tiene instalado por defe
# la versión de python que nosotros usaremos en nuestro proyecto, y también que la imagen que genera este sistema es pequeña.
FROM python:3.6.8-alpine

# En la etiqueta LABEL, mostraremos la información del desarrollador, y el email para el contacto
LABEL NataliaMartir <nataliamartir@correo.ugr.es>

# Establecemos con la etiqueta WORKDIR cual va a ser el directorio de trabajo
WORKDIR /src/

# Copiamos en la imagen los archivos que son necesarios nuestra api rest, este caso son:
COPY . ./

#Con el comando run queremos instalar lo necesario para que se pueda crear el contenedor, tendríamos la opción de usar
# requirements, pero podemos "RUN pip install --no-cache-dir -r requirements.txt" pero instalaria cosas que no son necesarias,
# por lo que solo instalaremos pip, y gunicorn --> Indicaremos que no se use la caché.
RUN pip install --upgrade pip && pip install --no-cache-dir -r gunicorn 

#Definimos el puerto donde el contenedor va a escuchar
EXPOSE 80

#Ejecutamos gunicorn
CMD cd src && gunicorn students-rest:app --bind 0.0.0.0:80
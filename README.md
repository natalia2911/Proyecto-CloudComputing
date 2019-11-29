[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.com/natalia2911/Proyecto-CloudComputing.svg?branch=master)](https://travis-ci.com/natalia2911/Proyecto-CloudComputing)
[![codecov](https://codecov.io/gh/natalia2911/Proyecto-CloudComputing/branch/master/graph/badge.svg)](https://codecov.io/gh/natalia2911/Proyecto-CloudComputing)
[![CircleCI](https://circleci.com/gh/natalia2911/Proyecto-CloudComputing.svg?style=svg)](https://circleci.com/gh/natalia2911/Proyecto-CloudComputing)
[![DevQAGRX](https://img.shields.io/badge/DevQAGRX-blueviolet?style=for-the-badge&logo=Git)](https://github.com/JJ/curso-tdd)
# Proyecto Cloud Computing


Este es el repositorio relacionado con el proyecto realizado por Natalia María Mártir Moreno sobre la asignatura de Cloud Computing del Máster de Ingeniería Informática de Granada.

## Prerequisitos

- **Versión**: Python 3.6.8
- **Dependecias**: pip install -r requirements.tx
- **Ejecución tests**: invoke test

## Descripción del proyecto
--- 
Nuestro proyecto es una aplicación encargada de gestionar mediante un calendario tanto los exámenes que pueda tener un alumno, como las asignaturas de las cuales esté matriculado. Todo esto se desarrollará en la nube.

***calendario personalizado para los alumnos de la ETSIIT***

[Información más detallada sobre el proyecto](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentación/DescripcionProyecto.md)

--- 

Nuestro proyecto se va a basar en una arquitectura de [microservicios](https://medium.com/@goodrebels/microservicios-ventajas-y-contras-de-la-arquitectura-descentralizada-a3b7fc814422). Cada uno de estos microservicios será independiente.


[Información sobre los microservicios](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentación/microservicios.md)


## Arquitectura

- `Lenguaje `: **Python** con herramienta de entorno virutal **virtualenv**.

- `Framework`:  **Django** 

- `Acceso a los datos` : **MongoDB**.

- `Comunicación`:  **[RabbitMQ](https://www.rabbitmq.com/)**

- `API Gateway`: **[KONG GATEWAY](https://konghq.com/kong/)** 

- `API Rest` : **Flask** 

- `Integración continua`: **pytest** y **invoke** 

- `Sistema de logging`:  libreria propia de python, llamada **logging**


[La justificación de la arquitectura](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentación/arquitectura_descrip.md)

[Historias de usuario](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentación/historias_usuario.md)


## Integración continua

Para la implementación de la integración continua utilizaremos dos servicios diferentes.

- **Travis-CI**: lo usamos para testear los microservicios descritos con anterioridad de forma sencilla, ya que este sistema nos permite conectar nuestro repositorio y con cada modificación que hagamos nos ejecute los test realizados, de tal forma que nos evitemos que se introduzcan errores no deseados y todo este completamente testeado en todo momento. Destacamos que estamos desarrollando nuestro proyecto en la versión **3.6.8** debido a que es la versión que usamos en local para el desarrollo, pero también probaremos con la versión *3.7* (Versión estable de python) y la *3.8*(Versión en desarrollo), todo sobre el sistema operativo Linux (Ubuntu 18)

- **Circle-CI**: usamos circle-ci como alternativa de sistema de integración continua, debido a su facilidad de uso, para ello tenemos el archivo de configuración [**.circleci/config.yml**](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/.circleci/config.yml)
    - En el usamos la versión 3.6.8, que es la versión con la que estamos desarrollando el proyecto en local. 

`Tenemos que destacar que parainstalar y testar las clases deberemos instalar las dependecias mediante los requirements.txt (pip install -r requirements.txt)`

Por otro lado como **herramienta de construcción** usaremos *[tasks.py](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/tasks.py)* de *Invoke*.

- Esta herramientas es usada para que todas las tareas se ejecuten de forma automática.

- Las diferentes tareas que ejecuta son:
    - La tarea **build** para instalar las dependencias.
    - La tarea **test** para que ejecute los test.
    - La tarea **codecov** para que envie los resultados al test de cobertura.

Tenemos que destacar que **Invoke** no será una dependencia de nuestro proyecto ya que lo usaremos como herramienta de construcción. 

buildtool: tasks.py

[Documentación adicional integración continua, explicación de la configuración](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/integracion_continua.md)

## Arquitectura por capas

Hemos decidido implementar uno de los microservicios descritos, en este caso el de **Gestión de Alumnos**
Tenemos una arquitectura por capas, ya que la hemos definido de esta forma:
- **Capa inferior**: donde tenemos la clase **Students.py** con su correspondiente test unitario **test_students.py** 
- **Capa superior**: donde tenemos la API REST del microservicio de gestión de alumnos en el fichero **students-rest.py** con su test de cobertura **test_students_rest.py**

# Uso de contenedores

Contenedor: https://hub.docker.com/r/natalia2911/proyecto-cloudcomputing

Hemos creado la imagen de nuestro contenedor apartir del [Dockerfile](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Dockerfile)

Como podemos ver, la imagen la hemos creado en [DockerHub](https://hub.docker.com/) 

Como parte adicional también hemos creado una imagen de nuestro contenedor en [Zeit](https://zeit.co/dashboard)

Imagen del contenedor de Zeit: https://proyecto-cloudcomputing.nataliamartir.now.sh/

[Documentación adiccional Zeit](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/doc-zeit.md)
[Documentación adiccional Docker](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/doc-docker.md)

## Depliegue de un PaaS

Para que nuestro servicio comience a funcionar, hemos elegido para desplegar nuestra aplicación Heroku.

He elegido esta plataforma debido a que: es gratis, permite tanto la integración con github, como con travis, y sobre todo por que es fácil de usar.

El despliege de la aplicación esta en esta url: https://students-rest.herokuapp.com/

[Documentación Heroku](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/doc-heroku.md)
## Licencia
---
Este proyecto tiene la licencia ***GNU General Public License v3.0*** debido a que es una de las licencias con más permisividad en el ámbito de estudiar, compartir o modificar el software.


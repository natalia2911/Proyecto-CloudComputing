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

Para la implementación de la integración continua utilizaremos dos servicios diferentes. **Travis-CI** y **Circle-CI**

buildtool: tasks.py

[Documentación adicional integración continua, explicación de la configuración](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/integracion_continua.md)

## Arquitectura por capas

https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/arquitectura_capas.md)

## Uso de contenedores

Contenedor: https://hub.docker.com/r/natalia2911/proyecto-cloudcomputing

Hemos creado la imagen de nuestro contenedor apartir del [Dockerfile](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Dockerfile)

Imagen del contenedor de Zeit: https://proyecto-cloudcomputing.nataliamartir.now.sh/

[Documentación adiccional Zeit](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/doc-zeit.md)
[Documentación adiccional Docker](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/doc-docker.md)

## Depliegue de un PaaS

Para que nuestro servicio comience a funcionar, hemos elegido para desplegar nuestra aplicación Heroku.

El despliege de la aplicación esta en esta url: https://students-rest.herokuapp.com/

[Documentación Heroku](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/doc-heroku.md)

## Despliegue del microservicio

Para desplegar el microservicio utilizaremos la herramienta de construcción `task.py` con invoke.

* Instalar dependencias: `invoke build`
* Ejecutar los test: `invoke test`
* Ejecutar test de cobertura: `invoke codevoc`
* Iniciar microservicio `invoke run -t "Numero de hebras" -w "Numero de workers"`
* Parar el microservicio `invoke stop`
* Construir la imagen de docker: `invoke docker`

## Almacenamiento de los datos

Para almacenar nuestros datos, como describimos en la parte de la arquitectura, usamos **MongoDB** más concretamente **Mongo Altas**, explicaremos con más detalle en la documentación como ha sido el proceso.

También hemos incluido la `inyección de dependecias` en relación con la base de datos.

Para más información consultar la documentación adicional.

[Documentación sobre la base de datos](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/basededatos.md)

## Prestaciones

Prestaciones: prestaciones_test.yml

En este caso hemos evaluado las prestaciones del microservicio *Students*.
Para proceder a evaluar las prestaciones del mismo hemos usado [Taurus](https://gettaurus.org/).
Se quería obtener un rendimiento de 1000 peticiones/s con 10 usuarios, pero el resultado que se ha obtenido ha sido de 1273.18Hits/segundo por lo que podemos decir que ha llegado a las prestaciones objetivo.

Para poder evaluar las prestaciones ejecutamos el comando `bzt prestaciones_test.yml -report`

[Documentación sobre las prestaciones](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/prestaciones.md)

## Próximamente ...

Estamos desarrollando el otro microservicio, el cúal integraremos también con la base de datos. 

Este se encontrará en el fichero: `Examns.py` con su correspondiente APIREST `examns-rest.py`

## Licencia
---
Este proyecto tiene la licencia ***GNU General Public License v3.0*** debido a que es una de las licencias con más permisividad en el ámbito de estudiar, compartir o modificar el software.


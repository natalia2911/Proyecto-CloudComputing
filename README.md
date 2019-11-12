[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Build Status](https://travis-ci.com/natalia2911/Proyecto-CloudComputing.svg?branch=master)](https://travis-ci.com/natalia2911/Proyecto-CloudComputing)
[![codecov](https://codecov.io/gh/natalia2911/Proyecto-CloudComputingbranch/master/graph/badge.svg)](https://codecov.io/gh/natalia2911/Proyecto-CloudComputing)
[![CircleCI](https://circleci.com/gh/natalia2911/Proyecto-CloudComputing.svg?style=svg)](https://circleci.com/gh/natalia2911/Proyecto-CloudComputing)
# Proyecto Cloud Computing


Este es el repositorio relacionado con el proyecto realizado por Natalia María Mártir Moreno sobre la asignatura de Cloud Computing del Máster de Ingeniería Informática de Granada.

## Prerequisitos

- **Versión**: Python 3.6.9
- **Dependecias**: pip install -r requirements.tx
- **Ejecución tests**: invoke test

## Descripción del proyecto
--- 
Nuestro proyecto es una aplicación encargada de gestionar mediante un calendario tanto los exámenes que pueda tener un alumno, como las asignaturas de las cuales esté matriculado. Todo esto se desarrollará en la nube.

***calendario personalizado para los alumnos de la ETSIIT***

[Información más detallada sobre el proyecto](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentación/DescripcionProyecto.md)

## Descripción de la arquitectura
--- 

Nuestro proyecto se va a basar en una arquitectura de [microservicios](https://medium.com/@goodrebels/microservicios-ventajas-y-contras-de-la-arquitectura-descentralizada-a3b7fc814422). Cada uno de estos microservicios será independiente.


Los microservicios que vamos a desarrollar son:

- `Gestión de exámenes`: accederá a la base de datos, y consultará los exámenes, las asignaturas asociadas a ese examen, el aula en el que se desarrollará, la fecha, el día, pudiendo también añadir una incidencia.

- `Gestión de alumnos`: accederán a la base de datos de los alumnos, y consultará los alumnos que están matriculados en una asignatura, pudiendo borrarse de ella, matricularse en otras.

- `Envío de mensajes`: se encargará de enviar mensajes.

### Diagrama de la arquitectura

![diagramaArquitectura](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/diagrama.png)

--- 

- `Lenguaje `: **Python** con herramienta de entorno virutal **virtualenv**.

- `Framework`:  **Django** 

- `Acceso a los datos` : **MongoDB**.

- `Comunicación`:  **[RabbitMQ](https://www.rabbitmq.com/)**

- `API Gateway`: **[KONG GATEWAY](https://konghq.com/kong/)** 

- `API Rest` : **Flask** 

- `Integración continua`: **pytest** y **invoke** 

- `Sistema de logging`:  libreria propia de python, llamada **logging**


![logosArquitecturas](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/arquitectura.png)

[La justificación de la arquitectura](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentación/arquitectura_descrip.md)

## Historias de usuario

Hemos definido las historias de usuario como milestones, en cada cúal contiene colgando de el issues con cada una de las funcionalidad de cada microservicio.

- [Funcionalidad del microservicio Gestión de alumnos](https://github.com/natalia2911/Proyecto-CloudComputing/milestone/6)
- [Funcionalidad del microservicio envio de mensajes](https://github.com/natalia2911/Proyecto-CloudComputing/milestone/7)
- [Funcionalidad del microservicio Gestión de exámenes](https://github.com/natalia2911/Proyecto-CloudComputing/milestone/5)




## Integración continua

Para la implementación de la integración continua utilizaremos dos servicios diferentes.

- **Travis-CI**: lo usamos para testear los microservicios descritos con anterioridad de forma sencilla, ya que este sistema nos permite conectar nuestro repositorio y con cada modificación que hagamos nos ejecute los test realizados, de tal forma que nos evitemos que se introduzcan errores no deseados y todo este completamente testeado en todo momento. Destacamos que estamos desarrollando nuestro proyecto en la versión *3.6.8*

- **Circle-CI**: usamos circle-ci como alternativa de sistema de integración continua, debido a su facilidad de uso, para ello tenemos el archivo de configuración [**.circleci/config.yml**](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/.circleci/config.yml)

Por otro lado como **herramienta de construcción** usaremos *Invoke* por lo que:

- Tendremos que instalar los *requirements.txt* 
- Para la ejecución de los test usaremos *pytest*
- Usaremos test de cobertura gestionados por *codecov*


buildtool: tasks.py

[Documentación adicional integración continua](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/integracion_continua.md)



## Licencia
---
Este proyecto tiene la licencia ***GNU General Public License v3.0*** debido a que es una de las licencias con más permisividad en el ámbito de estudiar, compartir o modificar el software.


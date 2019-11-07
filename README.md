[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
# Proyecto Cloud Computing


Este es el repositorio relacionado con el proyecto realizado por Natalia María Mártir Moreno sobre la asignatura de Cloud Computing del Máster de Ingeniería Informática de Granada.



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

- `Lenguaje `: **Python** .

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

## Licencia
---
Este proyecto tiene la licencia ***GNU General Public License v3.0*** debido a que es una de las licencias con más permisividad en el ámbito de estudiar, compartir o modificar el software.


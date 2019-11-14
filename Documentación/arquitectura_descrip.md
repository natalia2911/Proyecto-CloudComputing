# Descripción de la arquitectura

### Diagrama de la arquitectura

![diagramaArquitectura](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/diagrama.png)


Vamos a explicar la arquitectura que vamos a usar, y el por que hemos decidio usarla.

- `Lenguajes`: Al principio había decidido implementar cada servicio en un lenguaje diferente, pero por facilidad más tarde en la integración continua, he decidido implementar los microservicios en el mismo lenguaje **Python** .

` He decidido usar Python ya que es uno de los lenguajes más usados para la creación de microservicios y el que más librerías tiene para ello, y en el cuál más práctica tengo. `

Por otro lado decidimos usar la librería **SQLALCHEMY** ya que nos permite crear, modificar, consultar y eliminar nuestras tablas, así como crear, leer, actualizar y eliminar nuestros registros.

- `Framework`: Usaremos como framework **Django** para el desarrollo de la API REST, la cual contará con implementación de las peticiones HTTP tales como POST, GET, PUT, DELETE ..

`He decidido usar Django debido a que es un framework web de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático. Django hereda todas las características y facilidades que nos da Python, entre ellas escribir código bastante fácil de entender`

- `Acceso a los datos` :  Por otro lado hemos comentado que necesitaremos el acceso a una base de datos para toda la gestión de exámenes, asignaturas y alumnos por lo que una de las posibles candidatas podría ser **MongoDB**.

`Seleccionaremos MongoDB debido a que es una base de datos la cual es específica para tratar con documentos, y por que también es una base de datos no relacional. Esto será útil en nuestro proyecto ya que trataremos con los documentos de las matrículas, exámenes, etc.`


- `Comunicación`:  La comunicación entre los microservicios se va a realizar mediante paso de mensajes, para ello tendremos que implementar un sistema broker como por ejemplo **[RabbitMQ](https://www.rabbitmq.com/)**

`RabbitMQ es el intermediario de mensajes de código abierto más usado. Lo hemos elegido ya que es uno de los más ligeros y fáciles de implementar con microservicios en la nube, tiene un implementación distribuida y utiliza mensajería asíncrona. Lo hemos elegido debido a que es fácil de usar, soporta muchas plataformas de desarrollo, y puede recopilar varios servidores en un broker lógico.`

- `API Gateway`: uno de los servicios que utilizaremos en nuestra aplicación será una API Gateway, la usaremos debido a que esta actuará de enrutador desde la entrada hacia los microservicios.  Para ello hemos estado deliberando entre si usar traefik, kong, pero en definitiva nos hemos decantado por **[KONG GATEWAY](https://konghq.com/kong/)** 

`Lo hemos elegido debido a su funcionalidad, también por que esta apoyado en el servido HTTP Nginx, y debido a esto ofrece un alto rendimiento. También tenemos en cuenta que es open source.`


- `API Rest` : Cada servicio incluirá una API Rest y implementarla utilizaremos el microframework **Flask** 

`He decidido usar Flask ya que permite crear de forma sencilla una API REST, incluye un servidor web de desarrollo y tiene depurador y soporte integrado para pruebas unitarias, ademśa en compatible con Python 3.`

- `Integración continua`: Dentro de la parte de integración continua, hemos pensado que la forma más sencilla de llevarla a cabo es mediante la implementación de test con **pytest** y **invoke** como herramienta de ejecución de tareas.


- `Sistema de logging`: para gestionar los logs utilizaremos una libreria propia de python, llamada **logging** que nos permitirá rastrear un evento dentro de un software. Por ejemplo, registrar un mensaje de error.

![logosArquitecturas](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/arquitectura.png)
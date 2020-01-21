# Base de datos con MongoDB

Procedemos a integrar la base de datos a nuestra API REST.
Lo hemos hecho de dos formas distintas, una en local y otra en remoto.
En ambos casos hemos utilizado 'MongoDB' como se especifico en la descripción de la arquitectura.

## Versión local: MongoDB

Para la versión en local hemos instalado el cliente de Mongo en una versión '3.6.3', y una vez realizado esto nos conectamos al puerto 27017 que es el por defecto.
Esta url la almacenaremos en una variable de entorno llamada 'DB_BD', esta variable de entorno cambiará si queremos usar la base de datos en local (como en este caso), o en remoto.

![MongoLocal](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/mongo-local.png)

## Versión remota: MongoAltas

Lo primero que tenemos que hacer es crearnos una cuenta en MongoAtlas, y después elegir la configuración que queramos que tenga el cluster.
En este caso yo he elegido los servicios de amazón, y la región en la que era gratis, en este caso N.Virginia.

![MongoAtlas1](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/mongoatlas.png)

Como nos hemos registrado con la cuenta de la universidad, nos sale arriba que estamos en la universidad de granada.

![MongoAtlas1](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/mongo-cluster.png)

Por otro lado, yo para probar el microservicio también en local he añadido a 'COLLECTIONS' las colecciones de datos para probarlo.

![Colección de datos](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/coleccion.png)

También debemos crearnos un usuario y una contraseña, para luego poder conectarnos mediante esta url, que luego la meteremos como variable de entorno, modificando el usuario, y la contraseña por los valores reales.

![Conectar](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/conectar.png)

## Incluimos la base de datos al microservicio.

Para la inclusión de MongoDB a nuestro microservicio, hemos tenido que usar 'Pymongo' debido a que hemos utilizado python como lenguaje de nuestro microservicio.
Por un lado hemos creado la clase 'mongo_db.py' para luego mediante la **inyección de dependencias** incluirla al microservicio.

[Documentación sobre inyección dependencias](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/Documentaci%C3%B3n/inyeccion.md)

- Hemos modificado el 'Dockerfile' incluyendo la variable de entorno, también hemos actualizado la imagen en DockerHub.

```
#Variables de entorno: para la base de datos
ENV DB_BD ${DB_BD}
```

- En heroku, para que se pudiera conectar a mongoDB, lo tenía que hacer de manera remota por lo que, hemos incluido en nuestro contenedor de la siguiente manera:

```
heroku config:set DB_BD="url de mongoAtlas en remoto"
```

Por otro lado, en mongoAtlas también hemos tenido que permitir que se conecte a todas las IPs, para que así pudiera el contenedor acceder a los datos.

- En Travis, hemos tenido que añadir la variable de entorno mediante la página web.
- En el fichero de configuración de *Circle-CI* hemos tenido que añadir la imagen de mongo, y donde se va a conectar de forma local.
```
- image: mongo:3.6.3

environment:
MONGO_URL: mongodb://localhost:27017

```



# Evaluación de prestaciones

Para la evaluación de prestaciones hemos usado **Taurus**
Para ello hemos creado el fichero 'prestaciones_test.yml' y vamos a comentar lo que realiza.

'''
#Fichero de medición de prestaciones con Taurus:
execution:
- concurrency: 10 # Número de usuarios que se conectan
ramp-up: 10s # Tiempo en el que los usuarios se conectan
hold-for: 50s # Tiempo que el usuario tiene abierta la conexión
scenario: students-rest # Nombre del escenario, en nuestro caso de la APIREST.

# Escenarios
scenarios:
students-rest:
requests:
- url: http://localhost:8080/student
method: GET
- url: http://localhost:8080/bloqueado
method: GET
- url: http://localhost:8080/student/name/Pedro
method: GET
'''

Podemos ver que tenemos el servidor arrancando de manera local, con 10 usuarios que se conectaran en 10s y que la conexión se mantiene abierta 50s.
Por otro lado creamos el escenario para evaluar nuestra API-REST del microservicio Studend.
En el escenario realizamos 3 peticiones, las tres son peticiones GET, en la que 2 de ellas tendrán éxito y la petición de *bloqueado* será fallida con un código de error de HTTP 401, que indicará que está accediendo ha contenido no autorizado.

Hemos ejecutado dos pruebas, una con los datos de forma local, y otra con los datos en MongoAtlas.

Para ejecutar las pruebas, hemos realizado 4 intentos:

- Primer intento: 4 workers, con los datos de forma local.
- Segundo intento: 4 workers, con los datos en remoto.
- Tercer intento: 10 workers, con los datos de forma local.
- Cuarto intento: 10 workers, con los datos de forma remota.
- Quinto intento: sin base de datos.

## Primer intento: 4 workers, con los datos de forma local.

En este primer intento hemos utilizado 4 workers, y hemos usado los datos accediendo de forma local a mongoDB.
El resultado que hemos obtenido ha sido:

![Primer intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4-local.png)
![Primer intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4-local-report.png)

Como podemos ver no alcanzamos las peticiones que se pedían pero el resultado se aproxima al 50 por ciento, esto es debido a que accedemos a la base de datos de forma local.

## Segundo intento: 4 workers, con los datos en remoto.

En este segundo intento hemos utilizado 4 workers, y hemos usado los datos accediendo de forma remota a mongoDB, más concretamente hemos usado 'MongoAtlas'.
El resultado que hemos obtenido ha sido:

![Segundo intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4-remoto.png)
![Segundo intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4-remoto-report.png)

En este caso podemos ver que el número de peticiones baja considerablemente, hasta llegar a 27.7, lo cual es un número muy bajo.

## Tercer intento: 10 workers, con los datos de forma local.

En este tercer intento hemos utilizado 10 workers, y hemos usado los datos accediendo de forma local.
El resultado que hemos obtenido ha sido:

![Tercer intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/10-local.png)
![Tercer intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/10-local-report.png)

En este caso en número de peticiones que tenemos es similar al que teníamos con 4 workers.

## Cuarto intento: 10 workers, con los datos de forma remota.

En este cuarto intento hemos utilizado 10 workers, y hemos usado los datos accediendo de forma remota a mongoDB, más concretamente hemos usado 'MongoAtlas'.
El resultado que hemos obtenido ha sido:

![Cuarto intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4-remoto.png)
![Cuarto intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4-remoto-report.png)

Seguimos viendo, que los resultados son similares a cuando había 4 workers.

## Quinto intento: sin base de datos.

En este intento podemos ver que las prestaciones son mucho más altas, incluso hemos llegado a alcanzar 2424.6

![Quinto intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/sinBD.png)
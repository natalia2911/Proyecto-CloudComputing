# Evaluación de prestaciones

Para la evaluación de prestaciones hemos usado **Taurus**
Las prestaciones objetivo que queremos alcanzar son: 1000hits/s y con 10 usuarios ejecutandose de manera concurrente.
Para ello hemos creado el fichero 'prestaciones_test.yml' y vamos a comentar lo que realiza.

```
#Fichero de medicion de prestaciones con Taurus:
execution:
  - concurrency: 10 # Numero de usuarios que se conectan
    ramp-up: 10s    # Tiempo en el que los usuarios se conectan
    hold-for: 50s   # Tiempo que el usuario tiene abierta la conexión
    scenario: students-rest  # Nombre del escenario, en nuestro caso de la APIREST.

# Escenarios
scenarios:
  students-rest:
      requests:
        - url: http://0.0.0.0:8080/
          method: GET
          label: get-student #etiqueta
          assert: #Las aserciones se adjuntan a elementos de solicitud y se utilizan para establecer el estado de falla en la respuesta. El estado             de falla para la respuesta no es el mismo que el código de               respuesta para JMeter. 
          - contains: #verficiamos que puede estar el error 404
            - "200|404"
            subject: http-code
            regexp: true #Habilitamos que se puedan usar expresiones regulares.
```

Podemos ver que tenemos el servidor arrancando de manera local, con 10 usuarios que se conectaran en 10s y que la conexión se mantiene abierta 50s.
Por otro lado creamos el escenario para evaluar nuestra API-REST del microservicio Studend.
En el escenario realizamos 1 petición GET, en la que obtenemos todas las posibles opciones que puede presentarse en la API.

La prueba de las prestaciones la hemos hecho con la base de datos local, ya que con la base de datos en remoto, no alcanzamos las prestaciones objetivo.
Por otro lado, tambien destacamos que el despliege del servicio lo hemos hecho de forma local.

Para ejecutar las pruebas, hemos realizado 3 intentos:

- Primer intento: 4 workers ejecutandose en 1 hebra.
- Segundo intento: 4 workers ejecutandose en 2 hebras.
- Tercer intento: 10 workers ejecutandose en 2 hebras.


## Primer intento: 4 workers ejecutandose en 1 hebra.

En este primer intento hemos utilizado 4 workers, y una sola hebra, y podemos ver que el resultado que se obtiene es de 849.45 hits/s, podemos ver que el resultado no es malo del todo, pero podemos mejorar, ya que aún no llegamos a alcanzar las prestaciones requeridas.

![Primer intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4w-1h.png)


## Segundo intento: 4 workers ejecutandose en 2 hebras.

En este segundo intento hemos utilizado 4 workers y como diferencia del anterior intento hemos usado 2 hebras; hemos decido usar más hebras ya que creo que es una buena opción para mejorar las prestaciones.

Como podemos ver, si que han mejorado, superando el objetivo, como podemos ver el número de prestaciones que alcanza es de 1227.09Hits/s

![Segundo intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/4w-2h.png)


## Tercer intento: 10 workers ejecutandose en 2 hebras.

En este tercer intento, hemos decidido seguir usando 2 hebras, pero tambíen aumentar el número de workers a 10, de esta forma hemos alzancadoo un nivel de prestaciones de 1273.18Hits/segundo.

Es el mejor resultado en cuanto a prestaciones que hemos obtenido.

![Tercer intento](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/10w-2h.png)

### Errores cometidos

Al principio el nivel de prestaciones era de unos 400Hits/s aproximadamente y esto era debido a varios factores:
* Primero, usamos la base de datos de forma remota, con el acceso que tenemos a Mongo Atlas, y esto nos dió un nivel de prestaciones muy bajo.
* Por otro lado dentro del fichero de prestaciones, incluiamos escenarios de POST, y también nos dimos cuenta de que el nivel de prestaciones bajaba por este motivo, por lo que decidimos solo poner peticiones GET.

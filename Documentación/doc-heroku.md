# Despligue en Heroku

Docker:  https://students-rest.herokuapp.com/

Para el despliegue en Heroku, hemos creado el archivo `heroku.yml` el cual servirá para que Heroku cree la imagen a partir del Dockerfile.

```
build:
  docker:
    web: Dockerfile
run:
  web: cd src && gunicorn students-rest:app --log-file -

# Utilizamos --log-file para indicar el fichero de logs.
```

* `git add heroku.yml` Hacemos un commit
* Indicamos a Heroku, que nuestra app es un contenedor. `heroku stack:set container -a students-rest`
* Y hacemos el push `git push heroku master`

Dentro de la página de Heroku, linkeamos con nuestro Github, e indicamos nuestro repositorio.

Seleccionamos que nos haga el Deploy, de forma automática.


![img](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/heroku-1.png)

![img](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/heroku-2.png)

# Ejemplos:
* https://students-rest.herokuapp.com/ --> Devuelve {"status":"Ok"}

* https://students-rest.herokuapp.com/student/ --> Devuelve una lista con el contenido de todos los alumnos.

* http://students-rest.herokuapp.com/student/subject/ --> {"status":"Estamos dentro de la informacion de las asignaturas"}

* http://students-rest.herokuapp.com/student/subjects/name/Pedro --> {"InformacionSobreElAlumno":"\n\nPedro - 15520052C - Primero - CAL,IV,TID","status":"Estamos buscando por nombre"}


---

**Casos de errores:**

* http://students-rest.herokuapp.com/bloqueado/ --> HTTP 401.
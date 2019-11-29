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

* https://students-rest.herokuapp.com/student/ --> Devuelve {"status":"Estamos dentro de la informaci\u00f3n de los alumnos"}

* http://students-rest.herokuapp.com/student/subject/ --> {"status":"Estamos dentro de la informaci\u00f3n de las asignaturas"}

* http://students-rest.herokuapp.com/student/subjects/Pedro/15520052C/Primero --> {"InformacionSobreElAlumno":"Alumno:Pedro\n\nDNI: 15520052C\n\nCurso: Primero\n\nLista de asignaturas: CAL,IV,TID","Salida":"Este alumno si esta en nuestra base de datos"}

* https://students-rest.herokuapp.com/student/Pedro/15520052C/Primero --> {"InformacionSobreElAlumno":"Alumno: Pedro\n\nDNI: 15520052C\n\nCurso: Primero\n\n","Salida":"Este alumno si esta en nuestra base de datos"}

---

**Casos de errores:**

* https://students-rest.herokuapp.com/student/Pedro/15520052C/Primeroo --> {"InformacionSobreElAlumno":"El estudiante no aparece en nuestra lista de estudiantes","Salida":"No hay datos"}

* https://students-rest.herokuapp.com/student/subjects/Pedro/15520052C/Primeroo --> {"InformacionSobreElAlumno":"El estudiante no aparece en nuestra lista de estudiantes, por lo tanto no tiene asignaturas asociadas","Salida":"No hay datos"}
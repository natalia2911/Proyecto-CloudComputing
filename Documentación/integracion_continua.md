# Integración continua

Para incluir la integración continua dentro de nuestro proyecto, como hemos comentado antes lo haremos mediante dos sistemas diferentes: **Travis-CI** y **Circle-CI**

Para la puesta en marcha de cualquiera de los dos necesitamos código al cual le podamos pasar test, y los propios test.

## Para el caso de **Travis-CI**:

- Abrimos la página de [Travis-CI](https://travis-ci.com/) y vinculamos nuestro proyecto de Github para que pasen los test.
- Para que puedan pasarse los test, en nuestro repositorio tiene que aparecer el fichero de configuración de travis, llamado [.travis.yml](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/.travis.yml)
 . En dicho fichero como hemos comentado dentro de él en los comentarios especificaremos:

    -  El lenguaje utilizado, la versión de dicho lenguaje, la instalación de dependencias, los comandos para la ejecución de los test, y como parte adicional, pasamos los test a codecov, que es un test de cobertura, para que nos indique el porcentaje de código que este testeado.

``` # Lenguaje utilizado
language: python

# Para que nos ejecute los test de python en la versión correcta,
# aquí también podríamos probar con otras versiones.
python:
  - "3.6.8"

# Instalamos las dependencias
# Para la parte de los test de cobertura, instalamos codecov
install:
  - pip install -r requirements.txt
  - pip install codecov

# Ejecutamos los test con la herramienta de construcción
script:
   - invoke test
   - pytest --cov=./

#Pasamos los resultados del test a codecov.
after_success:
  - codecov
```

Ejemplo de funcionamiento de **Travis-CI**  ![FuncionamientoTravis](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/travis.png) 



## Para el caso de **Circle-CI**

- Tenemos que vincular nuestra cuenta de Github (El proyecto en sí) a la plataforma de [Circle-CI](https://circleci.com/gh/natalia2911/Proyecto-CloudComputing)
- Tenemos que añadir el fichero de configuración en una carpeta llamada *.circleci* y añadir un fichero llamado **config.yml**

    - En el fichero de configuración tendremos que indicar la versión de python que queremos que use para pasar los test, en este caso será la misma que en el fichero de travis, pero podríamos testear otras. Instalaremos las dependencias, y pasaremos los test.

```
version: 2
jobs:
  build:
    docker:
      - image: circleci/python:3.6.8
    steps:
      - checkout
      - run:
          name: Dependencias
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
      - run:
          name: Test
          command: |
            python3 -m venv venv
            . venv/bin/activate
            invoke test
```

La línea que introducimos antes de poner la instalación de dependencias o la ejecución del test:

 `python3 -m venv venv
            . venv/bin/activate`

La añadimos debido a que estamos trabajando con entornos virtuales `virtualenv` de python3, y sin ella no arrancaría la función run.

Ejemplo de funcionamiento de **Circle-CI**  ![FuncionamientoCircle](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/circleci.png)

# Test

Los test que hemos descrito para los diferentes microservicios son:

- Gestión de exámenes: 
    - Test_Asignatura: comprueba que la asignatura es correcta y está dentro de la lista de asignaturas.
    - Test_Fecha: comprueba que la fecha es correcta.
    - Test_Lugar: comprueba que el lugar del examen es correcto.

- Gestión de alumnos:
    - Test_Estudiante: comprueba que el nombre del alumno sea correcto, y está matriculado.
    - Test_ DNI: comprueba que el dni del alumno este registrado, y que tenga la longitud correcta.
    - Test_Curso: comprueba que el curso del alumno es el indicado en la matrícula.
    - Test_Asginatura: comprueba la lista de asignaturas que tiene el alumno matriculado sea la correcta.

# Test de cobertura

Hemos incluido como parte adicional unos test de cobertura, para que nos indique el porcentaje de código que está testeado.

Lo hacemos con **codecov**

Ejemplo de funcionamiento de **codecov**  ![FuncionamientoCodecov](https://github.com/natalia2911/Proyecto-CloudComputing/blob/master/img/codecov.png)
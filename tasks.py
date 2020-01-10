#!/usr/bin/python
# -*- coding: utf-8 -*-

from invoke import task,run

# Tarea que nos instala dependencias
@task
def build(n):
    n.run("pip install -r requirements.txt")

# Tarea que ejecuta los test
@task
def test(n):
    with n.cd('tests/'):
        n.run("pytest --cov=./")


# Tarea para ejecutar los test de cobertura
@task
def codecov(n):
    with n.cd('tests/'):
        n.run("codecov")

#Tarea para iniciar el microservicio, debido a que ahora
# solo tenemos uno lo que hacemos es que no implementamos la 
# opción de poner más que uno, el puerto por defecto es el 8080
# y podremos variar el número de workers.

@task
def run(n,port=8080,thereads=2,workers=10):
    with n.cd('src/'):
        n.run("gunicorn students-rest:app -t" + str(thereads) + " -w "+str(workers)+"  -b 0.0.0.0:"+str(port)+" &")

# Tarea para parar el microservicio
@task
def stop(n):
    n.run("pkill gunicorn")

#Tarea para hacer de forma automatica la contrucción de la imagen.

@task
def docker(n):
    n.run("docker build -t natalia2911/proyecto-cloudcomputing .")
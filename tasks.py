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

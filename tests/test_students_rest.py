import pytest, json, requests
from requests import *
import sys

sys.path.append('../src/')
sys.path.append('src')

url = 'https://students-rest.herokuapp.com/'

def test_raiz():
    response = requests.get(url)
    assert response.json()['status']=="Ok", "Estado correcto"

def test_status():
	response = requests.get(url+'/status')
	assert response.json()['status']=="OK"

def test_InfoStudent():
	response = requests.get(url+'/student/')
	assert response.json()['status']=="Estamos dentro de la lista de los alumnos"

def test_SubjectStudent():
	response = requests.get(url+'/student/subject/')
	assert response.json()['status']=="Estamos dentro de la informacion de las asignaturas"

def test_InfoStudentName():
	response = requests.get(url+'/student/name/')
	assert response.json()['status']=="Estamos buscando por nombre"

def test_InfoStudentDNI():
	response = requests.get(url+'/student/dni/')
	assert response.json()['status']=="Estamos buscando por dni"

def test_InfoStudentCurso():
	response = requests.get(url+'/student/curso/')
	assert response.json()['status']=="Estamos buscando por curso"



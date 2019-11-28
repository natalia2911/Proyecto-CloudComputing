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
	assert response.json()['status']=="Estamos dentro de la información de los alumnos"

def test_SubjectStudent():
	response = requests.get(url+'/student/subject/')
	assert response.json()['status']=="Estamos dentro de la información de las asignaturas"
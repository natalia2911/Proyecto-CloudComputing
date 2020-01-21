from flask import Flask, jsonify, abort
from Exams import Examns
from mongo_db import MongoDataBase
import os
import pymongo

# Código de error:
#401, no autorizado.
#403, prohibido.
#404, no encontrado.
#405, método no permitido.

examen = Examns('Calculo','20-01-2020','Aula01','Primero')

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def inicio():
	return jsonify(status="Ok")
    
@app.route('/bloqueado')
def bloqueado():
    return abort(401)

@app.route('/status',  methods = ['GET'])
def status():
	return jsonify(status="OK")

@app.route('/examns/',  methods = ['GET'])
def InicioExamenes():
    salida = examen.obtenerTodoExamenes()
    if salida == 'None':
        salida = abort(404)
    return jsonify(status="Estamos dentro de la lista de los examenes", ListadeExamenes=salida)

@app.route('/examns/subject/',  methods = ['GET'])
def InicioExams():
	return jsonify(status="Estamos dentro de la lista de los examenes - Introduce una asignatura para conocer el examen")

@app.route('/examns/subject/<asig>', methods = ['GET'])
def InfoExamAsig(asig):
    salida = examen.get_info_examn(asig)
    if salida == 'null':
        salida = abort(404)
    return jsonify(status="Estamos buscando por asignatura",InformacionSobreElAlumno = salida)

@app.route('/examns/fecha/<fecha>', methods = ['GET'])
def InfoExamFecha(fecha):
    salida = examen.get_info_fecha(fecha)
    if salida == 'null':
        salida = abort(404)
    return jsonify(status="Estamos buscando por fecha",InformacionSobreElAlumno = salida)

@app.route('/examns/curso/<curso>/', methods = ['GET'])
def InfoExamCurso(curso):
    salida = examen.get_info_curso(curso)
    if salida == 'null':
        salida = abort(404)
    return jsonify(status="Estamos buscando por curso",InformacionSobreElAlumno = salida)

@app.route('/examns/fecha/', methods = ['GET'])
def InfoExamnFecha_info():
    return jsonify(status="Estamos buscando por fecha")

@app.route('/examns/curso/', methods = ['GET'])
def InfoExamCurso_info():
    return jsonify(status="Estamos buscando por curso")

@app.route('/examns/delete/<subject>/', methods = ['DELETE'])
def eliminaExamen(subject):
    salida = examen.eliminarExamen(subject)
    return jsonify(status="Estamos borrando un examen",InformacionSobreElAlumno = salida)

if __name__ == "__main__":
    app.run(port='5000')
from flask import Flask, jsonify, abort
from Students import Students
from mongo_db import MongoDataBase
import os
import pymongo

# Código de error:
#401, no autorizado.
#403, prohibido.
#404, no encontrado.
#405, método no permitido.

db = MongoDataBase(url=os.environ['DB_BD'],database='ListaEstudiantes',collection='Estudiantes')

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

@app.route('/student/',  methods = ['GET'])
def InicioEstudiantes():
    salida = db.getAll()
    if salida == 'None':
        salida = abort(404)
    return jsonify(status="Estamos dentro de la lista de los alumnos", ListadeAlumnos=salida)

@app.route('/student/subject/',  methods = ['GET'])
def InicioAsignaturas():
	return jsonify(status="Estamos dentro de la informacion de las asignaturas")

@app.route('/student/name/<name>/', methods = ['GET'])
def InfoStudentName(name):
    salida = db.getStudentName(name)
    if salida == 'null':
        salida = abort(404)
    return jsonify(status="Estamos buscando por nombre",InformacionSobreElAlumno = salida)

@app.route('/student/dni/<dni>/', methods = ['GET'])
def InfoStudentDNI(dni):
    salida = db.getStudentDNI(dni) 
    if salida == 'null':
        salida = abort(404)
    return jsonify(status="Estamos buscando por dni",InformacionSobreElAlumno = salida)

@app.route('/student/curso/<curso>/', methods = ['GET'])
def InfoStudentCurso(curso):
    salida = db.getStudentCurso(curso)
    if salida == 'null':
        salida = abort(404)
    return jsonify(status="Estamos buscando por curso",InformacionSobreElAlumno = salida)

@app.route('/student/name/', methods = ['GET'])
def InfoStudentName_info():
    return jsonify(status="Estamos buscando por nombre")

@app.route('/student/dni/', methods = ['GET'])
def InfoStudentDNI_info():
    return jsonify(status="Estamos buscando por dni")

@app.route('/student/curso/', methods = ['GET'])
def InfoStudentCurso_info():
    return jsonify(status="Estamos buscando por curso")

@app.route('/student/delete/name/<name>/', methods = ['DELETE'])
def eliminaStudent(name):
    salida = db.eliminaNombre(name)
    return jsonify(status="Estamos borrando a un alumno",InformacionSobreElAlumno = salida)

@app.route('/student/insert/<name>/<dni>/<curso>/<asignaturas>/', methods = ['PUT'])
def insertarEstudiante(name,dni,curso,asignaturas):
    salida = db.insertarAlumno(name,dni,curso,asignaturas)
    return jsonify(status="Estamos borrando a un alumno",InformacionSobreElAlumno = salida)


if __name__ == "__main__":
    app.run(port='5000')
from flask import Flask, jsonify
from Exams import Exams
from SubjectList import SubjectList
from EnrolledStudentsList import EnrolledStudentsList
from ExamnList import ExamnList


enrolledstudents_list = EnrolledStudentsList()
subject_list = SubjectList()
lista = ExamnList()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def inicio():
	return jsonify(status="Ok")

@app.route('/status',  methods = ['GET'])
def status():
	return jsonify(status="OK")


@app.route('/exam/<subject>',  methods = ['GET'])
def InfoExam(subject):
    mensaje = "Esta asignatura no tiene ningun examen asociado"
    n = len(lista.subject)
    for i in range(n):
        if(subject == lista.subject[i]):
            examen = Exams(lista.subject[i], lista.date[i],subject_list ,lista.place[i])
            mensaje = examen.get_subject_exams(subject)
	
    return jsonify(Examen=mensaje)

# app.run(port='5000')
if __name__ == '__main__':
    app.run(port='5000')
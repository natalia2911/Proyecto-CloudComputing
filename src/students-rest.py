from flask import Flask, jsonify
from Students import Students
from SubjectList import SubjectList
from EnrolledStudentsList import EnrolledStudentsList

enrolledstudents_list = EnrolledStudentsList()
subject_list = SubjectList()

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def inicio():
	return jsonify(status="Ok")

@app.route('/status',  methods = ['GET'])
def status():
	return jsonify(status="OK")

@app.route('/student/', methods = ['GET'])
def InicioStudent():
	return jsonify(status="Estamos dentro de la información de los alumnos")

@app.route('/student/subject/',  methods = ['GET'])
def InicioAsignaturas():
	return jsonify(status="Estamos dentro de la información de las asignaturas")

@app.route('/student/<student>/<dni>/<curso>', methods = ['GET'])
def InfoStudent(student,dni,curso):
    estudiante = Students(student, dni, curso, enrolledstudents_list)
    n = len(enrolledstudents_list.name)
    salida = "El estudiante no aparece en nuestra lista de estudiantes"
    resultado = "No hay datos"
    for i in range(n):
        if(estudiante.name == enrolledstudents_list.name[i]):
            if(estudiante.course == enrolledstudents_list.curso[i] and estudiante.dni == enrolledstudents_list.dni[i]):
                salida = estudiante.get_info_student()
                resultado = "Este alumno si esta en nuestra base de datos"
    return jsonify(InformacionSobreElAlumno=salida, Salida=resultado )

@app.route('/student/subjects/<student>/<dni>/<curso>', methods = ['GET'])
def InfoSubjectStudent(student,dni,curso):
    estudiante = Students(student, dni, curso, enrolledstudents_list)
    n = len(enrolledstudents_list.name)
    salida = "El estudiante no aparece en nuestra lista de estudiantes, por lo tanto no tiene asignaturas asociadas"
    resultado = "No hay datos"
    for i in range(n):
        if(estudiante.name == enrolledstudents_list.name[i]):
            if(estudiante.course == enrolledstudents_list.curso[i] and estudiante.dni == enrolledstudents_list.dni[i]):
                salida = estudiante.get_info_subject()

                resultado = "Este alumno si esta en nuestra base de datos"
    return jsonify(InformacionSobreElAlumno=salida, Salida=resultado )

if __name__ == '__main__':
     app.run(port='5000')

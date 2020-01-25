from mongo_db import MongoDataBase
from EnrolledStudentsList import EnrolledStudentsList

import pymongo
import os

estudiantes = {
    EnrolledStudentsList('Pedro','15520052C','Primero','CAL,IV,TID'),
    EnrolledStudentsList('Juan','15520053C','Segundo','CAL,IV,TID,CC,PDOO'),
    EnrolledStudentsList('Alicia','15520054C','Tercero','CAL,IC,ALG,FIS,TDD'),
    EnrolledStudentsList('Natalia','15520055C','Cuarto','TDD,PDOO,IV'),
    EnrolledStudentsList('Laura','15520056C','Quinto','IA,CC'),
}

db = MongoDataBase(url=os.environ['DB_BD'],database='ListaEstudiantes',collection='Estudiantes',datos=estudiantes)



class Students:
    def __init__(self, name, dni, curso, asignaturas):
       self.name = name
       self.dni = dni
       self.curso = curso
       self.asignaturas = asignaturas

    def __str__(self):
        return "Nombre: %s - Dni: %s - Curso: %s - Asignaturas: %s" \
               %(self.name, self.dni, self.curso, self.asignaturas)

    def obtenerTodo(self):
        salida = db.getAll()
        return salida
    
    def get_info_student_name(self,name):
        salida = db.getStudentName(name)
        return salida

    def get_info_student_dni(self,dni):
        salida = db.getStudentDNI(dni)
        return salida

    def get_info_student_curso(self,curso):
        salida = db.getStudentCurso(curso)
        return salida
    
    def eliminarEstudiante(name):
        salida = db.eliminaNombre(name)
        return salida
    





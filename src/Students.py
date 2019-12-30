from mongo_db import MongoDataBase
from EnrolledStudentsList import EnrolledStudentsList

import pymongo
import os

db = MongoDataBase(url=os.environ['DB_BD'],database='ListaEstudiantes',collection='Estudiantes')

class Students:
    def __init__(self, name, dni, curso, asignaturas):
       self.name = name
       self.dni = dni
       self.curso = curso
       self.asignaturas = asignaturas

    def __str__(self):
        return "Nombre: %s - Dni: %s - Curso: %s - Asignaturas: %s" \
               %(self.name, self.dni, self.curso, self.asignaturas)

    def get_info_student_name(self,name):
        salida = db.getStudentName(name)
        return salida

    def get_info_student_dni(self,dni):
        salida = db.getStudentDNI(dni)
        return salida

    def get_info_student_curso(self,curso):
        salida = db.getStudentCurso(curso)
        return salida
    

if __name__ == "__main__":
    estudiante = Students('Pedro','15520052C','Primero','CAL,IV,TID')
    print(estudiante.get_info_student_curso('155203C'))




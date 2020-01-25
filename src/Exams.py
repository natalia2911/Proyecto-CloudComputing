from mongo_db import MongoDataBase
from ExamnList import ExamnList

import pymongo
import os

examenes = {
    ExamnList('Calculo','20-01-2020','Aula01','Primero'),
    ExamnList('Redes','21-01-2020','Aula02','Segundo'),
    ExamnList('IV','22-01-2020','Aula03','Tercero'),
    ExamnList('CC','23-01-2020','Aula04','Cuarto'),
}

db = MongoDataBase(url=os.environ['DB_BD'],database='ListaExamenes',collection='Examenes',datos=examenes)

class Examns:
    def __init__(self, subject, fecha, aula, curso):
       self.subject = subject
       self.fecha = fecha
       self.aula = aula
       self.curso = curso

    def __str__(self):
        return "Asignatura %s - Fecha: %s - Aula: %s - Curso: %s" \
               %(self.subject, self.fecha, self.aula, self.curso)

    def obtenerTodoExamenes(self):
        salida = db.getAllExamen()
        return salida
    
    def get_info_examn(self,subject):
        salida = db.getExam(subject)
        return salida

    def get_info_fecha(self,fecha):
        salida = db.getExamFecha(fecha)
        return salida

    def get_info_curso(self,curso):
        salida = db.getExamCurso(curso)
        return salida

    def get_info_aula(self,aula):
        salida = db.getExamAula(aula)
        return salida
    
    def eliminarExamen(subject):
        salida = db.eliminaExam(name)
        return salida

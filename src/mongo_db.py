import pymongo
from EnrolledStudentsList import EnrolledStudentsList
from ExamnList import ExamnList
from bson.objectid import ObjectId
import os

class MongoDataBase:
    def __init__(self,url,database,collection,datos):
        # PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
        self.mongoClient = pymongo.MongoClient(url)
        # PASO 2: Conexión a la base de datos
        self.db = self.mongoClient[database]
        # PASO 3: Obtenemos una coleccion para trabajar con ella
        self.collection = self.db[collection]
        if(self.collection == 'Estudiantes'):
            for estudiante in self.datos:
                self.collection.insert_one(estudiante.toDBColletion())
        
        if(self.collection == 'Examenes'):
            for examen in self.datos:
                self.collection.insert_one(examen.toDBColletion())
        

# Para la base de datos de Estudiantes
#------------------------------------------------------------------------------------------------------

# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
    def getAll(self):
        cursor = self.collection.find()
        salida = "\n\n"
        for est in cursor:
            salida = salida + "  " + est['name'] + " - " + est['dni'] + " - " + est['curso'] + " - " + est['asignaturas']
        return salida

    def getStudentName(self,name):
        cursor = self.collection.find({"name":{"$in":[name]}})
        salida= '\n\n'
        for est in cursor:
            salida = salida + est['name'] + " - " + est['dni'] + " - " + est['curso'] + " - " + est['asignaturas']
            return salida

    def getStudentDNI(self,dni):
        cursor = self.collection.find({"dni":{"$in":[dni]}})
        salida= 'none'
        for est in cursor:
            salida = est['name'] + " - " + est['dni'] + " - " + est['curso'] + " - " + est['asignaturas']
            return salida

    def getStudentCurso(self,curso):
        cursor = self.collection.find({"curso":{"$in":[curso]}})
        salida= '\n\n'
        for est in cursor:
            print(est)
            salida = salida + est['name'] + " - " + est['dni'] + " - " + est['curso'] + " - " + est['asignaturas']
            return salida

    def eliminaNombre(self,name):
        self.collection.remove({"name":name})
        return "El alumno ha sido borrado"
 
    def eliminaDNI(self,dni):
        self.collection.remove({"dni":dni})
        return "El alumno ha sido borrado"
        


# Para la base de datos de Examenes
#------------------------------------------------------------------------------------------------------

    def getAllExamen(self):
        cursor = self.collection.find()
        salida = "\n\n"
        for est in cursor:
            #print(est['name'] + " - " + est['dni'] + " - " + est['curso'] + " - " + est['asignaturas'])
            salida = salida + "  " + est['subject'] + " - " + est['fecha'] + " - " + est['aula'] + " - " + est['curso']
        return salida

    def getExam(self,subject):
        cursor = self.collection.find({"subject":{"$in":[subject]}})
        salida= '\n\n'
        for est in cursor:
            salida = salida + est['subject'] + " - " + est['fecha'] + " - " + est['aula'] + " - " + est['curso']
            return salida

    def getExamFecha(self,fecha):
        cursor = self.collection.find({"fecha":{"$in":[fecha]}})
        salida= 'none'
        for est in cursor:
            salida = est['subject'] + " - " + est['fecha'] + " - " + est['aula'] + " - " + est['curso']
            return salida

    def getExamCurso(self,curso):
        cursor = self.collection.find({"curso":{"$in":[curso]}})
        salida= '\n\n'
        for est in cursor:
            print(est)
            salida = salida + est['subject'] + " - " + est['fecha'] + " - " + est['aula'] + " - " + est['curso']
            return salida

    def getExamAula(self,aula):
        cursor = self.collection.find({"aula":{"$in":[aula]}})
        salida= '\n\n'
        for est in cursor:
            salida = salida + est['subject'] + " - " + est['fecha'] + " - " + est['aula'] + " - " + est['curso']
            return salida

    def eliminaExam(self,subject):
        self.collection.remove({"subject":subject})
        return "Examen borrado"
 
    

if __name__ == "__main__":
    pass
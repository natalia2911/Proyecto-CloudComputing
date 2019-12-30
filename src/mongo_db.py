import pymongo
from EnrolledStudentsList import EnrolledStudentsList
from bson.objectid import ObjectId

estudiantes = {
    EnrolledStudentsList('Pedro','15520052C','Primero','CAL,IV,TID'),
    EnrolledStudentsList('Juan','15520053C','Segundo','CAL,IV,TID,CC,PDOO'),
    EnrolledStudentsList('Alicia','15520054C','Tercero','CAL,IC,ALG,FIS,TDD'),
    EnrolledStudentsList('Natalia','15520055C','Cuarto','TDD,PDOO,IV'),
    EnrolledStudentsList('Laura','15520056C','Quinto','IA,CC'),
}

MONGODB_HOST = 'localhost'
MONGODB_PORT = '27017'
MONGODB_TIMEOUT = 1000


URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"

class MongoDataBase:
    def __init__(self,database,collection):
        # PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
        self.mongoClient = pymongo.MongoClient('mongodb://localhost:27017/')
        # PASO 2: Conexión a la base de datos
        self.db = self.mongoClient[database]
        # PASO 3: Obtenemos una coleccion para trabajar con ella
        self.collection = self.db[collection]

        for estudiante in estudiantes:
            self.collection.insert_one(estudiante.toDBColletion())


# PASO 4.2.1: "READ" -> Leemos todos los documentos de la base de datos
    def getAll(self):
        cursor = self.collection.find()
        salida = "\n\n"
        for est in cursor:
            #print(est['name'] + " - " + est['dni'] + " - " + est['curso'] + " - " + est['asignaturas'])
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



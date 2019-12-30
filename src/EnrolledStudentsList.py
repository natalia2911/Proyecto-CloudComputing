
class EnrolledStudentsList:

    def __init__(self,name,dni,curso,asignaturas):
        self.name = name
        self.dni = dni
        self.curso = curso
        self.asignaturas = asignaturas
       

    def toDBColletion (self):
        return{
            "name":self.name,
            "dni":self.dni,
            "curso":self.curso,
            "asignaturas":self.asignaturas
        }
    def __str__(self):
        return "Nombre: %s - Dni: %s - Curso: %s - Asignaturas: %s" \
               %(self.name, self.dni, self.curso, self.asignaturas)



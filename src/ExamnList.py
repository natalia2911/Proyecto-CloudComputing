class ExamnList:

    def __init__(self, subject, fecha, aula, curso):
       self.subject = subject
       self.fecha = fecha
       self.aula = aula
       self.curso = curso

    def toDBColletion (self):
        return{
            "subject":self.subject,
            "fecha":self.fecha,
            "aula":self.aula,
            "curso":self.curso
        }
    def __str__(self):
        return "Asignatura %s - Fecha: %s - Aula: %s - Curso: %s" \
               %(self.subject, self.fecha, self.aula, self.curso)



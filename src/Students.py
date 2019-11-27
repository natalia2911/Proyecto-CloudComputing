from SubjectList import SubjectList
from EnrolledStudentsList import EnrolledStudentsList

subjects_list = SubjectList()
enrolledstudents_list = EnrolledStudentsList()


class Students:
    def __init__(self, name, dni, course, enrolledstudents_list):
       self.name = name
       self.dni = dni
       self.course = course
       self.enrolledstudents_list = enrolledstudents_list

       if not name in self.enrolledstudents_list.name:
           raise ValueError("Este alumno no esta matriculado")

    def get_info_student(self):
        msg = "Alumno: " + self.name + "\n\n"  + "DNI: " + self.dni + "\n\n" + "Curso: " + self.course + "\n\n"
        return msg

    def get_info_subjects(self):
        msg = "Alumno:" + self.name + "\n\n"  + "DNI: " + self.dni  + "\n\n" + "Lista de asignaturas: "  
        n = len(subjects_list.subjects)
        for i in range(n):
            msg += subjects_list.subjects[i] + " "
        return msg

    def get_info_subject(self):
        msg = "Alumno:" + self.name + "\n\n"  + "DNI: " + self.dni + "\n\n" + "Curso: " + self.course + "\n\n" + "Lista de asignaturas: "  
        n = len(enrolledstudents_list.asignaturas)
        for i in range(n):
            if(self.name == enrolledstudents_list.name[i]):
                msg += enrolledstudents_list.asignaturas[i]
        return msg

    def push_subject(self, subject):
        pass
  

    



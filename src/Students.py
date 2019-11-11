from SubjectList import SubjectList
from EnrolledStudentsList import EnrolledStudentsList

class Students:
    def __init__(self, name, dni, course, enrolledstudents_list):
       self.name = name
       self.dni = dni
       self.course = course
       self.enrolledstudents_list = enrolledstudents_list

       if not name in self.enrolledstudents_list.name:
           raise ValueError("Este alumno no esta matriculado")

    def get_info_student(self):
        msg = self.name + "\n\n"  + "DNI: " + self.dni + "\n\n" + "Curso: " + self.course + "\n\n"
        return msg


  
if __name__ == "__main__":
    failed_student = "Pedro"
    dni = "15520052"
    course = "Primero"
    enrolledstudents_list = EnrolledStudentsList()
    student = Students(failed_student, dni, course, enrolledstudents_list)
    msg = student.get_info_student()
    print(msg)

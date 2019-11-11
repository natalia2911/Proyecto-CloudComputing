import pytest
import sys
sys.path.append('../src/')
sys.path.append('src')

from Students import Students
from SubjectList import SubjectList
from EnrolledStudentsList import EnrolledStudentsList

result_simple = {
    """
    Alumno: Natalia

    DNI: 15520052

    Curso: Primero 
    """
}


enrolledstudents_list = EnrolledStudentsList()
subject_list = SubjectList()

def test_failed_student():
    failed_student = "Pedro"
    dni = "15520052"
    course = "Primero"
    estudiante = Students(failed_student, dni, course, enrolledstudents_list)
    msg = estudiante.get_info_student()
    with pytest.raises(ValueError):
        assert msg == result_simple


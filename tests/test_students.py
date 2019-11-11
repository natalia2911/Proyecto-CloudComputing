import pytest
import sys
sys.path.append('../src/')
sys.path.append('src')

from Students import Students
from SubjectList import SubjectList
from EnrolledStudentsList import EnrolledStudentsList

result = "Alumno: Natalia\n\nDNI: 15520052C\n\nCurso: Primero\n\n"
result2= "Alumno: Natalia\n\nDNI: 15520052C\n\nLista de asignaturas: CAL IV IA SCD"

enrolledstudents_list = EnrolledStudentsList()
subject_list = SubjectList()

def test_failed_student():
    failed_student = "Pepe"
    dni = "15520052C"
    course = "Primero"

    with pytest.raises(ValueError):
        estudiante = Students(failed_student, dni, course, enrolledstudents_list)
        assert estudiante.get_info_student() == result

def test_failed_dni():
    student = "Natalia"
    failed_dni = "1552005"
    course = "Primero"

    numero_dni = 9
    n_in_dni = len(failed_dni)

    assert numero_dni != n_in_dni

def test_failed_course():
    student = "Natalia"
    dni = "15520052C"
    failed_course = "Segundo"

    estudiante = Students(student, dni, failed_course, enrolledstudents_list)
    assert estudiante.get_info_student() != result

def test_subjects():
    student = "Natalia"
    dni = "15520052C"
    course = "Primero"
    estudiante = Students(student, dni, course, enrolledstudents_list)
    assert estudiante.get_info_subjects != result2



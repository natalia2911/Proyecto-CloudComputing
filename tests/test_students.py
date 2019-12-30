import pytest
import sys
sys.path.append('../src/')
sys.path.append('src')

from Students import Students

def test_failed_student():
    failed_student = "Luis"
    dni = "15520052C"
    course = "Primero"
    asignaturas = 'CAL,IV,TID'
    result = 'None'

    estudiante = Students(failed_student, dni, course, asignaturas)
    assert estudiante.get_info_student_name(failed_student) != result

def test_failed_dni():
    student = "Natalia"
    failed_dni = "1552005"
    course = "Primero"

    numero_dni = 9
    n_in_dni = len(failed_dni)

    assert numero_dni != n_in_dni

def test_dni():
    name = "Pedro"
    dni = "15520053C"
    course = "Primero"
    asignaturas = 'CAL,IV,TID'
    result = 'None'

    estudiante = Students(name, dni, course, asignaturas)
    assert estudiante.get_info_student_dni(dni) != result

def test_failed_course():
    name = "Pedro"
    dni = "15520053C"
    course = "Segundo"
    asignaturas = 'CAL,IV,TID'
    result = 'None'


    estudiante = Students(name, dni, course, asignaturas)
    assert estudiante.get_info_student_curso(course) != result



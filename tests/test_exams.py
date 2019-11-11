import pytest
import sys
sys.path.append('../src/')
sys.path.append('src')

from Exams import Exams
from SubjectList import SubjectList

result = {
    """
    Examen de la asignatura CC

    Fecha: 01/02/2020

    Lugar: Sala de usos multiples"""
}

subject_list = SubjectList()

def test_failed_subject():
    failed_subject = "STOP"
    date = "01/02/2020"
    place = "Sala de usos multiples"

    with pytest.raises(ValueError):
        exam = Exams(failed_subject,date,subject_list,place)
        assert exam.get_subject_exam == result

def test_failed_date():
    subject = "CC"
    failed_date = "23/23/23"
    place = "Sala de usos multiples"

    with pytest.raises(ValueError):
        exam = Exams(subject,failed_date,subject_list,place)
        assert exam.get_subject_exam == result

def test_failed_place():
    subject = "CC"
    date = "01/02/2020"
    failed_place = "En mi casa"

    with pytest.raises(ValueError):
        exam = Exams(subject,date,subject_list,failed_place)


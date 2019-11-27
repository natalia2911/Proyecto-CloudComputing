import pytest
import sys
sys.path.append('../src/')
sys.path.append('src')

from Exams import Exams
from SubjectList import SubjectList

result = "Examen de la asignatura: CC\n\nFecha: 01/02/2020\n\nLugar: Sala de usos multiples\n\n"

subject_list = SubjectList()

def test_failed_subject():
    failed_subject = "STOP"
    date = "01/02/2020"
    place = "Sala de usos multiples"

    with pytest.raises(ValueError):
        exam = Exams(failed_subject,date,subject_list,place)
        assert exam.get_subject_exam() == result

def test_failed_date():
    subject = "CC"
    failed_date = "23/23/23"
    place = "Sala de usos multiples"
    exam = Exams(subject,failed_date,subject_list,place)
    with pytest.raises(TypeError) as e:
        raise TypeError(result)
        assert str(exam.get_subject_exam()) != result

def test_failed_place():
    subject = "CC"
    date = "01/02/2020"
    failed_place = "En mi casa"

    with pytest.raises(TypeError) as e:
        raise TypeError(result)
        exam = Exams(subject,date,subject_list,failed_place)

if __name__ == "__main__":
    subject = "CC"
    failed_date = "23/23/23"
    place = "Sala de usos multiples"
    exam = Exams(subject,failed_date,subject_list,place)
    print(exam.get_subject_exam())
    print(result)


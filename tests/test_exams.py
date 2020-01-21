import pytest
import sys
sys.path.append('../src/')
sys.path.append('src')

from Exams import Examns
from ExamnList import ExamnList


def test_failed_subject():
    failed_subject = "CCC"
    fecha = "20-01-2020"
    aula = "Aula01"
    curso = "Primero"
    result = 'None'

    examen = Examns(failed_subject,fecha,aula,curso)
    assert examen.get_info_examn(failed_subject) != result

def test_failed_fecha():
    subject = "Calculo"
    failed_fecha = "20-02-2020"
    aula = "Aula01"
    curso = "Primero"
    result = 'None'

    examen = Examns(subject,failed_fecha,aula,curso)
    assert examen.get_info_fecha(failed_fecha) != result

def test_failed_aula():
    subject = "Calculo"
    fecha = "20-01-2020"
    failed_aula = "Aula044"
    curso = "Primero"
    result = 'None'

    examen = Examns(subject,fecha,failed_aula,curso)
    assert examen.get_info_aula(failed_aula) != result

def test_failed_curso():
    subject = "Calculo"
    fecha = "20-01-2020"
    aula = "Aula01"
    failed_curso = "asdf"
    result = 'None'

    examen = Examns(subject,fecha,aula,failed_curso)
    assert examen.get_info_curso(failed_curso) != result

if __name__ == "__main__":
    pass


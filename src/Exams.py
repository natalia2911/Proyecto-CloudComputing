from SubjectList import SubjectList

class Exams:
    def __init__(self, subject, date, subjects_list,place):
        self.subjects_list = subjects_list
        if not subject in self.subjects_list.subjects:
            raise ValueError("No se encuentra dicha asignatura")
        self.subject = subject
        self.date = date
        self.place = place

    def get_subject_exam(self):
        msg = "Examen de la asignatura: " + self.subject + "\n\n" + "Fecha: " + self.date + "\n\n" + "Lugar: " + self.place + "\n\n"
        return msg

    def info_error_exams(self,exam1,exam2):
        if exam1.date == exam2.date:
            raise ValueError("Los examenes se solapan")
    def push_exam(self):
        pass



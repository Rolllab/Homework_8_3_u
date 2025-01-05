from teacher import Teacher

class DisciplineTeacher(Teacher):
    def __init__(self, name, lastname, education, experience, discipline, job_title):
        super().__init__(name=name, lastname=lastname, education=education, experience=experience)
        self.__discipline = discipline
        self.__job_title = job_title

    @property
    def get_discipline(self):
        return self.__discipline

    @property
    def get_job_title(self):
        return self.__job_title

    @get_job_title.setter
    def get_job_title(self, item):
        self.__job_title = item

    def get_teacher_data_in_discipline(self) -> str:
        return f'{self.get_teacher_data()}\nПредмет {self.__discipline}, должность {self.__job_title}'

    def add_mark_in_discipline(self, name:str, lastname:str, grade:int) -> str:
        return f'{self.add_mark(student_name=name, student_lastname=lastname, grade=grade)}\nПредмет: {self.__discipline}'

    def remove_mark_in_discipline(self, name:str, lastname:str, grade:int) -> str:
        return f'{self.remove_mark(student_name=name, student_lastname=lastname, grade=grade)}\nПредмет: {self.__discipline}'

    def give_a_consultation_in_discipline(self, group:str) -> str:
        return f'{self.give_a_consultation(group=group)}\nПо предмету {self.__discipline} как {self.__job_title}'
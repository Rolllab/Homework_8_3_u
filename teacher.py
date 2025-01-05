class Teacher:
    def __init__(self, name, lastname, education, experience):
        self.__name = name
        self.__lastname = lastname
        self.__education = education
        self.__experience = experience

    @property
    def get_name(self):
        return self.__name

    @property
    def get_lastname(self):
        return self.__lastname

    @property
    def get_education(self):
        return self.__education

    @property
    def get_experience(self):
        return self.__experience

    @get_experience.setter
    def get_experience(self, item):
        self.__experience = item

    def get_teacher_data(self) -> str:
        return (f'{self.get_name} {self.get_lastname}, образование {self.get_education}, '
                f'опыт работы {self.get_experience} года')

    def add_mark(self, student_name:str, student_lastname:str, grade:int) -> str:
        return f'{self.get_name} {self.get_lastname} поставил оценку {grade} студенту {student_name} {student_lastname}'

    def remove_mark(self, student_name:str, student_lastname:str, grade:int) -> str:
        return f'{self.get_name} {self.get_lastname} удалил оценку {grade} студенту {student_name} {student_lastname}'

    def give_a_consultation(self, group:str) -> str:
        return f'{self.get_name} {self.get_lastname} провел консультацию в классе {group}'
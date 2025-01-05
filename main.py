from discipline import DisciplineTeacher
from linkedlist import LinkedList



if __name__ == '__main__':
    dt0 = DisciplineTeacher(name='Егор', lastname='Петросян', education='высшее', experience=25, discipline='', job_title='директор')
    dt1 = DisciplineTeacher(name='Иван', lastname='Иванов', education='высшее', experience=2, discipline='физкультура', job_title='учитель')
    dt2 = DisciplineTeacher(name='Степан', lastname='Метелкин', education='высшее', experience=3, discipline='алгебра', job_title='учитель')
    dt3 = DisciplineTeacher(name='Изольда', lastname='Ква-ква', education='средне-специальное', experience=7, discipline='история', job_title='учитель')
    dt4 = DisciplineTeacher(name='Пух', lastname='Степанов', education='высшее', experience=1, discipline='химия', job_title='учитель')

    teachers_list = LinkedList()
    teachers_list.append(dt0)
    teachers_list.append(dt1)
    teachers_list.append(dt2)
    teachers_list.append(dt3)
    teachers_list.append(dt4)


    print("Список персонала:")
    teachers_list.view_data()

    # Удаление учителя
    teachers_list.pop(dt3)

    print("\nСписок персонала после удаления:")
    teachers_list.view_data()


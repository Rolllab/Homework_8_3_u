""" Если запуск теста осуществлять через терминал, то только командами -
        python3 -m unittest discover -s tests                   - обычное тестирование
        python -m coverage run -m unittest discover -s tests    - тестирование с покрытием
        python -m coverage report                               - рапорт покрытия
        python -m coverage html                                 - отчет в HTML
                                                """



from unittest import TestCase
import io
from contextlib import redirect_stdout

from linkedlist import LinkedList
from discipline import DisciplineTeacher



class TestLinkedList(TestCase):
    def setUp(self):
        self.ll = LinkedList()

        self.t1 = DisciplineTeacher(name="Иван", lastname="Иванов", education="высшее", experience=2,
                                    discipline="физкультура", job_title="учитель")
        self.t2 = DisciplineTeacher(name="Степан", lastname="Метелкин", education="высшее", experience=3,
                                    discipline="алгебра", job_title="учитель")
        self.t3 = DisciplineTeacher(name="Изольда", lastname="Ква-ква", education="средне-специальное",
                                          experience=7, discipline="история", job_title="учитель")


    def test_append(self):
        self.ll.append(self.t1)
        self.ll.append(self.t2)
        self.ll.append(self.t3)

        self.assertEqual(self.ll.head.data, self.t1)
        self.assertEqual(self.ll.head.next_node.data, self.t2)
        self.assertEqual(self.ll.head.next_node.next_node.data, self.t3)

    def test_pop(self):
        self.ll.append(self.t1)
        self.ll.append(self.t2)
        self.ll.append(self.t3)

        self.ll.pop(self.t3)
        self.assertEqual(self.ll.head.next_node.next_node, None)


    def test_pop_empty_list(self):
        self.assertEqual(self.ll.pop(self.t1), None)

    def test_pop_teacher_not_found(self):
        self.ll.append(self.t1)
        self.ll.append(self.t3)

        self.assertEqual(self.ll.pop(self.t2), None)

    def test_view_data(self):
        """Тестирование метода display_teachers."""
        self.ll.append(self.t1)
        self.ll.append(self.t2)

        output = io.StringIO()
        with redirect_stdout(output):
            self.ll.view_data()

        self.assertEqual("\tучитель: Иванов Иван, дисциплина: физкультура\n\tучитель: Метелкин Степан, дисциплина: алгебра\n", output.getvalue())


class TestDisciplineTeacher(TestCase):
    def setUp(self):
        self.dt = DisciplineTeacher(name="Иван", lastname="Иванов", education="высшее", experience=2,
                                    discipline="физкультура", job_title="учитель")

    def test_get_teacher_data_in_discipline(self):
        self.assertEqual(self.dt.get_teacher_data(), 'Иван Иванов, образование высшее, опыт работы 2 года')

    def test_add_mark_in_discipline(self):
        name, lastname, grade = 'name', 'lastname', 34
        self.assertEqual(self.dt.add_mark_in_discipline(name=name, lastname=lastname, grade=grade), 'Иван Иванов поставил оценку 34 студенту name lastname\nПредмет: физкультура')


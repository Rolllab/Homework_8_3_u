class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    """Создание одно-связанного списка"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Вставляет данные в начало списка"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node


    def pop(self, data):
        if self.head is None:
            print("Список пуст...")
            return

        if self.head.data == data:
            self.head = self.head.next_node
            print(f"Учитель {data.get_name}, {data.get_lastname} удалён.")
            return

        current_node = self.head
        while current_node.next_node and current_node.next_node.data != data:
            current_node = current_node.next_node

        if current_node.next_node is None:
            print("Данных нет...")
        else:
            current_node.next_node = current_node.next_node.next_node
            print(f"\nУчитель {data.get_name}, {data.get_lastname} удалён.")

    def view_data(self):
        if self.head is None:
            print("Список пустой...")
            return

        current_node = self.head
        while current_node:
            data = current_node.data
            print(f"\t{data.get_job_title}: {data.get_lastname} {data.get_name}, дисциплина: {data.get_discipline}")
            current_node = current_node.next_node
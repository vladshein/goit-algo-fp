#Final project task1
"""
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.
"""
class Node:
    def __init__(self, data: int=None):
        self.data = data  # Зберігає дані вузла
        self.next = None  # Посилання на наступний вузол

class LinkedList:
    def __init__(self):
        self.head = None  # Початок списку, спочатку пустий

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = self.head  # Вказує, що новий вузол має посилатися на поточний головний вузол
        self.head = new_node  # Робить новий вузол головним вузлом списку

    def insert_at_end(self, data):
        new_node = Node(data)  # Створює новий вузол з даними
        if self.head is None:  # Якщо список пустий
            self.head = new_node  # Робить новий вузол головним вузлом
        else:
            cur = self.head  # Починає з головного вузла
            while cur.next:  # Проходить до кінця списку
                cur = cur.next
            cur.next = new_node  # Додає новий вузол в кінці списку

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:  # Перевіряє, чи існує попередній вузол
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)  # Створює новий вузол з даними
        new_node.next = prev_node.next  # Вказує, що новий вузол має посилатися на вузол після попереднього вузла
        prev_node.next = new_node  # Вставляє новий вузол після попереднього вузла

    def delete_node(self, key: int):
        cur = self.head  # Починає з головного вузла
        if cur and cur.data == key:  # Якщо головний вузол містить потрібні дані
            self.head = cur.next  # Робить наступний вузол головним
            cur = None  # Видаляє вузол
            return
        prev = None  # Змінна для зберігання попереднього вузла
        while cur and cur.data != key:  # Проходить список у пошуках потрібних даних
            prev = cur
            cur = cur.next
        if cur is None:  # Якщо вузол з потрібними даними не знайдено
            return
        prev.next = cur.next  # Видаляє вузол з потрібними даними
        cur = None  # Звільняє пам'ять, видаляючи вузол

    def search_element(self, data: int) -> Node | None:
        cur = self.head  # Починає з головного вузла
        while cur:  # Проходить список у пошуках потрібних даних
            if cur.data == data:  # Якщо знайдено потрібні дані
                return cur  # Повертає вузол з потрібними даними
            cur = cur.next
        return None  # Якщо вузол з потрібними даними не знайдено

    def print_list(self):
        current = self.head  # Починає з головного вузла
        while current:  # Проходить весь список
            print(current.data, end=" -> ")  # Виводить дані вузла
            current = current.next  # Переходить до наступного вузла
        print("None")  # Вказує на кінець списку

    def reverse_ll(self):
        # Тимчасові змінні
        prev = None
        current = self.head
         
        # Пройтись по списку і змінити направлення 
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        # Головою стає останній елемент початкового списку
        self.head = prev

    # Функція для сортування зв'язного списку
    def sort_ll(self):
        # Тимчасові змінні для відсортованого зв'язного списку та поточного вузла
        sorted_list = None
        current = self.head
        
        # Поки не буде пройдений весь список
        while current:
            # наступний вузол буде некст з поточного
            next_node = current.next
            # виклик внутрішньої функції для опрацювання поточного вузла і додавання його в відсортований список
            sorted_list = self.sorted_insert(sorted_list, current)
            # наступний вузол стає поточним
            current = next_node
        # запишемо результат сортування в атрибут класу
        self.head = sorted_list

    # Внутрішня функція для сортуваня зв'язного списку
    def sorted_insert(self, sorted_list, new_node):
        if not sorted_list or sorted_list.data >= new_node.data:
            new_node.next = sorted_list
            sorted_list = new_node
        else:
            current = sorted_list
        
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return sorted_list

# Функція для злиття двох відсортованих зв'язних списків
def merge_two_sorted_lists(list1: LinkedList, list2: LinkedList):
    dummy = Node(0)
    tail = dummy
    # Поки один з двох списків не дійде кінця вибрати менше значення і додати до нового списку
    while list1 and list2:
        if list1.data < list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # Якщо один з двох списків не дійшов кінця, додати його в злитий список
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    
    return dummy.next
    
        

if __name__ == '__main__':
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(13)
    llist.insert_at_beginning(100)
    llist.insert_at_beginning(-10)
    llist.insert_at_beginning(15)
    llist.print_list()
    
    llist.reverse_ll()
    print("\nПеревернутий зв'зний список:")
    llist.print_list()

    llist.sort_ll()
    print("\nВідсортований список:")
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_beginning(5)
    llist2.insert_at_beginning(1)
    llist2.insert_at_beginning(13)
    
    print("\nДодаємо другий зв'язний список:")
    llist2.print_list()
    llist2.sort_ll()
    print("\nВідсортований другий список:")
    llist2.print_list()

    merged_list = LinkedList()
    merged_head = merge_two_sorted_lists(llist.head, llist2.head)
    merged_list.head = merged_head
    
    print("\nЗливаеємо два відсортовані списки:")
    merged_list.print_list()

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("\nЗв'язний список:")
    llist.print_list()

    # Видаляємо вузол
    llist.delete_node(10)

    print("\n Зв'язний список після видалення вузла з даними 10:")
    llist.print_list()

    # Пошук елемента у зв'язному списку
    print("\n Шукаємо елемент 10:")
    element = llist.search_element(10)
    print(element.data) if element else print("Такого значення в списку немає")

    print("\n Шукаємо елемент 100:")
    element = llist.search_element(100)
    print(element.data) if element else print("Такого значення в списку немає")
# Q.  링크드 리스트의 모든 원소를 출력하시오

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



        print("출력해보세요!")

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()
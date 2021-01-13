# Q.  링크드 리스트에서 index 번째 원소를 제거하시오.

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

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):  # [3]-> [5] -> [12] 에서 [5]-> [12]로 만들어줘야함
        if index == 0:                #index가 0번째일경우
            self.head = self.head.next #head에 다음 숫자를 넣어라
            return
        node = self.get_node(index-1)
        node.next = node.next.next  #기존 연결을 끊은 후 다음 다음으로 연결을 시켜라

        return node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.delete_node(0)   # 3을 삭제후 5->12만 출력
linked_list.print_all()
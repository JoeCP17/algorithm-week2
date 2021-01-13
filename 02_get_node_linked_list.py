# Q.  링크드 리스트에서 index번째 원소를 반환하시오.


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

    def get_node(self, index):   #index번째의 의미 = next_node로 가는거를 인덱스번 해야한다는 의미
        node = self.head    # node 변수에 머릿수 self.head 삽입
        count = 0           # node가 진행됨에 따라 읽어야하는 번호
        while count < index:  # count가 index보다 작으면
            node = node.next  # node를 next로 이동시켜라
            count += 1        # count에는 1씩을 더하고

        return node
# 0번째 5가 들어가 있고 1번째 12가 들어가 있다.

linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(0).data)  # -> 5를 들고 있는 노드를 반환해야 합니다!

# 노드안에 들어가는것 : 각 노드가 데이터랑 다음칸에 있는 포인터
# data , next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 맨처음 생성할때는 아무것도 다음을 가리키지 않기때문


node = Node(3)
first_node = Node(4)
node.next = first_node


# print(node.next.data) # 기존 node [3] 의 다음값 [4]의 데이터 값을 표현한것

class Linkedlist:  # 링크드 리스트에는 헤드노드만 가지고있으면됨
    def __init__(self, data):
        self.head = Node(data)

    def append(self,data):
        cur = self.head
        while cur.next is not None:  #맨 마지막 부분이 None이기때문에 그전까지 반복해서 cur을 이동
            cur = cur.next #계속하여 next값을 넣어준다.


        cur.next = Node(data) # next값에 값들을 계속 넣어준다.
        print(cur.data)

    def print_all(self):
        print("hihihi")
        cur = self.head
        while cur is not None:  #None으로 가기전까지 반복시킨다.
            print(cur.data)
            cur = cur.next





linked_list = Linkedlist(3)

linked_list.append(4) # 다음부분에 4를 삽입
linked_list.append(5)# 그 다음 next에 5를 삽입
linked_list.print_all()
# head만을 출력할시 => Node 출력
# head.data 출력시 => 3 출력

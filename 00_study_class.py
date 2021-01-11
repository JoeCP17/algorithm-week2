class person:
    def __init__(self, param_name):  # 생성자를 생성하기 위해서 쓰이는 함수
        print("I am created", self)
        self.name = param_name
        #self : 자기자신을 넘겨주는데 굳이 적지 않아도 파이썬 자체에서 넘겨준다.
        #init : 생성되었을때 쓰는 함수

    def talk(self): # name 출력함수
        print("안녕하세요,제 이름은 ",self.name,"입니다.")


person_1 = person("유재석")
print(person_1)
print(person_1.name)
person_1.talk()
person_2 = person("박명수")
print(person_2.name)
print(person_2)
person_2.talk()

# () : 생성자를 의미한다. 즉 새로운 객체를 생성할때 쓰는 함수


# class Node:
#     def __init__(self, data):
#         self.data(클래스의 데이터) = data (파라미터의 데이터)
#         self.next = None

#3을 가진 node     node = Node(3)
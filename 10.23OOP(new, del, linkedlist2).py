#new
class Point:
    def __init__(self, x=0, y=0):
        print("__init__ call")
        self.x = x
        self.y = y

    def __new__(cls, *args, **kwargs):
        print(f"__new__ call of {cls} with params: {args} and {kwargs}")
        return super().__new__(cls)

pt = Point(1, 2)
pt = Point(1, 2)
print(pt)



#del
class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connection with db {self.user}, {self.psw}, {self.port}")

db1 = DataBase('root1', '1234', 80)
db2 = DataBase('root2', '56', 40)
db3 = DataBase('root3', '78', 40)

#coming last result from db3:
print(id(db1))
print(id(db2))

db1.connect()
db2.connect()



#Linkedlist2
#node1:
#   data = 2
#   next = node2:
#               data = 5
#               next = None
#node1.next.next = node3
#               next = node3:
#                           data = 9
#                           next = None
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()


linked = LinkedList()
linked.append(2) # HEAD
#TAIL
linked.append(5)
linked.append(9)

linked.display()
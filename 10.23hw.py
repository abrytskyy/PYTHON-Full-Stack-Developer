# class Friend:
#     def __init__(self, name,surname, friend):
#         self.name = name
#         self.surname = surname
#         self.friend = friend
#
#
# friends = Friend("Tom", "Brown", Friend("Bob", "Black", Friend("Sam", "Test", None)))
#
# print(f"{friends.name} {friends.surname} -> {friends.friend.name} {friends.friend.surname} -> {friends.friend.friend.name} {friends.friend.friend.surname}")
# current = tom
# current = tom.friend




# delete last
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
            last_el = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                last_el = current.next
            current.next = new_node

    def display(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def delete(self):
        if not self.head:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next is not None and current.next.next:
            current = current.next
        current.next = None


linked = LinkedList()
linked.append(2)  # HEAD
# TAIL
linked.append(5)
linked.append(9)

linked.display()
linked.delete()
linked.display()




# Linked list is a data structure.
# Linked lists are series of connected nodes.
# Each node stores the data and the address of the next node.
# Address of the first node is named Head.
# Address of the last node points to null.
# Linked list are the most effeicient data structure.
# Operations: Search, Insert, and Delete.
# Time complexity: Searching: O(n), Insert: O(1), and Delete: O(1).


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = Node()

    def add(self, data):

        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
    
    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):

        if index >= self.length():
            print("Index out of range.")
            return None
        current_idx = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_idx == index:
                return current_node.data
            current_idx += 1

    def delete(self, index):

        if index >= self.length():
            print("Index out of range.")
            return
        current_idx = 0 
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if index == current_idx:
                last_node.next = current_node.next
                return
            current_idx += 1


my_list = LinkedList()

my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(4)
print("length", my_list.length())
print("Elements and 3rd index is", my_list.get(3))
my_list.display()
my_list.delete(2)
my_list.display()


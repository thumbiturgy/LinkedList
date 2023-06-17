from Node import Node

class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current_node = self.head
        while current_node.right:
            current_node = current_node.right
        current_node.right = node

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right
    
    def __repr__(self):
        return ' -> '.join(node.value for node in self)
    
    def insert_node(self, target, value):
        new_node = Node(value)
        if self.head:
            for node in self:
                if node.value == target:
                    right_node = node.right
                    node.right = new_node
                    new_node.right = right_node
        else:
            print('Empty List')

    def remove_node(self, value):
        if value == self.head.value:
            self.head = self.head.right
        else:
            for node in self:
                if node.right.value == value:
                    node.right = node.right.right
                    return

    def get_tail(self):
        # for node in self:
        #     pass
        # return node.value
        node = self.head
        while node.right:
            node = node.right
        return node.value
    
    def remove_tail(self):
        node = self.head
        if node.right:
            while node.right.right:
                node = node.right
            node.right = None
    
    def add_list_elements(self, adds_list):
        for item in adds_list:
            self.add_node(item)

linked_list = LinkedList()


linked_list.add_node('Sunday')
linked_list.add_node('Monday')
linked_list.add_node('Tuesday')
linked_list.add_node('Thursday')

print(linked_list)

linked_list.insert_node('Tuesday', 'Wednesday')

print(linked_list)

linked_list.add_node('Spazday')
linked_list.remove_node('Sunday')
linked_list.remove_node('Spazday')
print(linked_list)

print(linked_list)

linked_list.remove_tail()

print(linked_list)
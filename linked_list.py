class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """класс для хранения односвязного списка"""
    def __init__(self):
        self.head = None

    def insert_beginning(self, data: dict):
        self.head = Node(data, self.head)

    def insert_at_end(self, data: dict):
        if self.head is None:
            self.head = Node(data, None)

        var = self.head
        while var.next_node:
            var = var.next_node

        var.next_node = Node(data, None)

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()

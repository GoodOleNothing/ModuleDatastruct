class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.data_list = []

    def enqueue(self, data):
        self.data_list.append(data)
        self.head = Node(self.data_list[0], self.tail)
        self.tail = Node(self.data_list[len(self.data_list) - 1])


#queue = Queue()
#queue.enqueue('data1')
#queue.enqueue('data2')
#queue.enqueue('data3')
#
#print(queue.head.data)
#print(queue.head.next_node.data)
#print(queue.tail.data)
#print(queue.tail.next_node)
#print(queue.tail.next_node.data)



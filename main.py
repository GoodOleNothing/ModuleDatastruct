class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None
        self.old_top = []

    def push(self, new_data):
        new_node = self.top
        new_top = Node(new_data, new_node)
        self.old_top.append(new_top)
        self.top = self.old_top[len(self.old_top) - 2]
    def pop(self):
        self.top = None
        return self.old_top[len(self.old_top) - 1].data


#n1 = Node(5, None)
#n2 = Node('a', n1)
#print(n1.data)
#print(n2.data)
#print(n1)
#print(n2.next_node)
#stack = Stack()
#stack.push('data1')
#stack.push('data2')
#stack.push('data3')
#print(stack.top.data)
#print(stack.top.next_node.data)
#print(stack.top.next_node.next_node.data)
#print(stack.top.next_node.next_node.next_node)
#print(stack.top.next_node.next_node.next_node.data)

stack = Stack()
stack.push('data1')
data = stack.pop()
print(stack.top)
print(data)

stack = Stack()
stack.push('data1')
stack.push('data2')
#stack.push('data3')
#stack.push('data4')
print(stack.top.data)
data = stack.pop()
print(data)

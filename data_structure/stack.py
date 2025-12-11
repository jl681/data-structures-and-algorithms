class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height >= 1:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height >= 1:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp
        else:
            return None


if __name__ == '__main__':
    stack = Stack(2)
    stack.push(1)
    stack.print_stack()
    stack.pop()
    stack.print_stack()

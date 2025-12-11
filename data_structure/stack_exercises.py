class StackUseList:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def is_balanced_parentheses(input_str):
    my_stack = StackUseList()
    if len(input_str) == 0:
        return True
    for s in input_str:
        if s == "(":
            my_stack.push(s)
        else:
            if my_stack.is_empty() or my_stack.pop() != '(':
                return False
    return my_stack.is_empty()


def reverse_string(input_str):
    my_stack = StackUseList()
    result = ''
    if len(input_str) == 0:
        return result
    for s in input_str:
        my_stack.push(s)
    while my_stack.size() > 0:
        result += my_stack.pop()
    return result


def sort_stack(test_stack: StackUseList):
    # 创建一个辅助栈
    temp_stack = StackUseList()

    # 遍历原栈中的元素
    while not test_stack.is_empty():
        # 弹出原栈的元素
        current_element = test_stack.pop()

        # 将元素插入辅助栈的正确位置
        while not temp_stack.is_empty() and temp_stack.peek() > current_element:
            test_stack.push(temp_stack.pop())
        temp_stack.push(current_element)

    # 将辅助栈的元素弹回原栈
    while not temp_stack.is_empty():
        test_stack.push(temp_stack.pop())

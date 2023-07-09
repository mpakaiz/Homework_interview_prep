class Stack:

    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        pop_element = self.stack.pop()
        return pop_element

    def peek(self):
        return self.stack[-1]

    def size(self):
        size = len(self.stack)
        return size

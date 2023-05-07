class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length += 1
        return self

    def peek(self):
        if self.length == 0:
            return None
        return self.top

    def pop(self):
        if self.length == 0:
            return None
        holdingPointer = self.top
        self.top = self.top.next
        self.length -= 1
        return self
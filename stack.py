class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '{value:' + self.value + ', next:' + str(self.next) + '}'


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __repr__(self):
        return '{top' + str(self.top) + '}'

    def peek(self):
        return self.top

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

    def pop(self):
        if self.top == self.bottom:
            self.bottom = None
        holdingPointer = self.top
        self.top = self.top.next
        self.length -= 1
        return self

myStack = Stack()
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.push('Test Pop')
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack)
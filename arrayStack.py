class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    # def __repr__(self):
    #     return str()

class Stack:
    def __init__(self):
        self.array = []

    def __repr__(self):
        return 'Stack { array: ' + str(self.array) + ' }'

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self, value):
        self.array.append(value)
        return self

    def pop(self):
        self.array.pop()
        return self

myStack = Stack()
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
# myStack.push('Test Pop')
# myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
# print(myStack.peek())
print(myStack)
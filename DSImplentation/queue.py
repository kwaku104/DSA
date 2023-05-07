class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return '{ value: ' + self.value + ', next: ' + str(self.next) + '}'


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __repr__(self):
        return '{ first: Node ' + str(self.first) + ', last: Node' + str(self.last) + '}'

    def peek(self):
        if self.length == 0:
            return None
        return self.first

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self

    def dequeue(self):
        if not self.first:
            return None
        if self.first == self.last:
            self.last == None
        self.first = self.first.next
        self.length -= 1
        return self


myQueue = Queue()
print(myQueue.enqueue('Joy'))
print(myQueue.enqueue('Matt'))
print(myQueue.enqueue('Pavel'))
print(myQueue.enqueue('Samir'))
print(myQueue.peek())

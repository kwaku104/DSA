class CrazyQueue:
    def __init__(self):
        self.first = []
        self.last = []

    def __repr__(self):
        return 'CrazyQueue { first:' + str(self.first) + ', last :' + str(self.last) + ' }'

    def enqueue(self, value):
        length = len(self.first)
        for i in self.first:
            self.last.append(self.first.pop())
        self.last.append(value)
        return self

    def dequeue(self):
        length = len(self.last)
        for i in self.last:
            self.first.append(self.last.pop())
        self.first.pop()
        return self

    def peek(self):
        if len(self.last) > 0:
            return self.last[0]
        return self.first

myQueue = CrazyQueue()
myQueue.peek()
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
print(myQueue.enqueue('Pavel'))
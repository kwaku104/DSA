# 5 - -> 10 - -> 3 - -> 20


class LinkedList():
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        self.tail[next] = newNode
        self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = {
            'value': value,
            'next': None
        }

        newNode[next] = self.head
        self.head = newNode
        self.length += 1

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode['next']
            counter += 1
        return currentNode

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)

        if index == 0:
            return self.prepend(value)

        newNode = {
            'value': value,
            'next': None
        }

        leader = self.traverseToIndex(index - 1)
        holdingPointer = leader['next']
        leader['next'] = newNode
        newNode['next'] = holdingPointer
        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head['next']
        leader = self.traverseToIndex(index - 1)
        unwantedNode = leader['next']
        leader['next'] = unwantedNode['next']
        self.length -= 1

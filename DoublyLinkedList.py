# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value':value,
            'next':None,
            'previous': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        # newNode = Node(value)
        newNode = {
            'value': value,
            'next': None,
            'previous': None
            }
        newNode['previous'] = self.tail
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = {
            'value':value,
            'next': None,
            'previous': None
        }
        newNode['next'] = self.head
        self.head['previous'] = newNode
        self.head = newNode
        self.length += 1
        return self

    def printList(self):
        arrayList = []
        currentNode = self.head
        while currentNode != None:
            arrayList.append(currentNode['value'])
            currentNode = currentNode['next']
        return arrayList

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)

        if index == 0:
            self.prepend(value)
            return self.printList()

        newNode = {
            'value':value,
            'next': None,
            'previous':None
        }

        leader = self.traverseToIndex(index-1)
        follower = leader['next']
        leader['next'] = newNode
        newNode['next'] = follower
        follower['previous'] = newNode
        self.length += 1
        print(self)
        return self.printList()

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode['next']
            counter += 1
        return currentNode

    def remove(self, index):
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader['next']
        leader['next'] = unwantedNode['next']
        follower = leader['next']
        follower['previous'] = leader
        self.length -= 1
        return self.printList()

    def reverse(self):
        if not self.head['next']:
            return self.head

        first = self.head
        self.tail = self.head
        second = first['next']
        while second:
            temp = second['next']
            second['next'] = first
            first = second
            second = temp
        self.head['next'] = None
        self.head = first
        return self.printList()




myLinkedList = LinkedList(10)
# print(myLinkedList.__init__)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2,99)
myLinkedList.insert(20,88)
print(myLinkedList.remove(2))
# print(myLinkedList.remove(2))
print(myLinkedList.printList())
print(myLinkedList.reverse())
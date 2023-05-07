# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value':value,
            'next':None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        # newNode = Node(value)
        newNode = {
            'value': value,
            'next': None
            }
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        # print(self.head)
        # print(self.tail)
        # print(self.length)
        return self

    def prepend(self, value):
        newNode = {
            'value':value,
            'next': None
        }
        newNode['next'] = self.head
        self.head = newNode
        self.length += 1

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
            'next': None
        }

        leader = self.traverseToIndex(index-1)
        holdingPointer = leader['next']
        leader['next'] = newNode
        newNode['next'] = holdingPointer
        self.length += 1
        return self.printList()

    def traverseToIndex(self, index):
        counter = 0
        currentNode = self.head
        while counter != index:
            currentNode = currentNode['next']
            counter += 1
        return currentNode

    def remove(self, index):
        if index == 0:
            self.head = self.head['next']
            return self.printList()
        leader = self.traverseToIndex(index-1)
        unwantedNode = leader['next']
        leader['next'] = unwantedNode['next']
        self.length -= 1
        return self.printList()

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            # next = current['next']
            # current['next'] = prev
            # prev = current
            # current = next
            curr = self.head['next']
            print("curr" , curr)
            current['next'] = self.head
            print(current['next'])
            self.head = self.head['next']
            print(self.head)
        # self.head = prev
        return self.printList()

    def NthNodeEndOfList(self, index):
        pass





myLinkedList = LinkedList(10)
# print(myLinkedList.__init__)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2,99)
myLinkedList.insert(20,88)
myLinkedList.remove(2)
print(myLinkedList.remove(0))
print(myLinkedList.reverse())
# print(myLinkedList.printList())
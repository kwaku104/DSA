class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.data

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def deleteAtIndex(self, index):
        item = self.data[index]
        self.shiftItems(index)
        print(self.data)
        return item

    def shiftItems(self, index):
        for i in range(self.length - 1):
            self.data[i] = self.data[i + 1]
        print(self.data[self.length - 1])
        del self.data[self.length - 1]
        self.length -= 1


MyArray = MyArray()
print(MyArray.push('hi'))
MyArray.push('you')
MyArray.push('!')
MyArray.pop()
MyArray.deleteAtIndex(0)
MyArray.push('are')
print(MyArray.push('nice'))

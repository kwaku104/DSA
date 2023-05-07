# # class Node:
# #     def __init__(self, value):
# #         self.value = value
# #         self.next = None


# class MultiStack:
#     def __init__(self, stackSize):
#         self.stackCapacity = stackSize
#         self.values = []
#         self.sizes = [0,0,0]
#         self.numberOfStacks = 3

#     def stackCapacity(self):
#         return self.stackCapacity

#     def push(self, stackNumber, value):
#         if self.isFull(stackNumber):
#             return "Stack number {} is full".format(stackNumber)
#         self.sizes[stackNumber] += 1
#         self.values[self.indexOfTop(stackNumber)] = value
#         return "item {} has been successfully added to stack {}".format(value, stackNumber)

#     def pop(self, stackNumber):
#         if self.isEmpty(stackNumber):
#             return "Stack number {} is empty".format(stackNumber)
#         topIndex = self.indexOfTop(stackNumber)
#         value = self.values[topIndex]
#         self.values[topIndex] = 0
#         self.sizes[stackNumber] -= 1
#         return value

#     def peek(self, stackNumber):
#         if self.isEmpty(stackNumber):
#             return "Stack number {} is empty".format(stackNumber)
#         topIndex = self.indexOfTop(stackNumber)
#         return self.values[topIndex]

#     def isEmpty(self, stackNumber):
#         return self.sizes[stackNumber] == 0

#     def isFull(self, stackNumber):
#         return self.sizes[stackNumber] == self.stackCapacity

#     def indexOfTop(self, stackNumber):
#         offset = stackNumber * self.stackCapacity
#         size = self.sizes[stackNumber]
#         return offset + size



# stack = MultiStack(5)
# print(stack.stackCapacity)
# print(stack.indexOfTop(0))
# print(stack.values)
# print(stack.push(0, 3))

class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


def ThreeInOne():
    newstack = MultiStack(2)
    print (newstack.IsEmpty(1))
    newstack.Push(3, 1)
    print (newstack.Peek(1))
    print (newstack.IsEmpty(1))
    newstack.Push(2, 1)
    print (newstack.Peek(1))
    print (newstack.Pop(1))
    print (newstack.Peek(1))
    newstack.Push(3, 1)

ThreeInOne()
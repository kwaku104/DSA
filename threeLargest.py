def findThreeLargest(array):
    threeLargest = [None,None,None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate() #TODO
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate() #TODO
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate() #TODO

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
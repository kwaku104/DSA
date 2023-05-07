def compress(chars):
    firstIdx = 0
    secondIdx = 0
    curOne = chars[0]
    numOfChar = 0
    while(secondIdx < len(chars)):
        if chars[secondIdx] == curOne:
            numOfChar += 1
        if chars[secondIdx] != curOne or secondIdx == len(chars)-1:
            if(numOfChar != 1):
                strNum = str(numOfChar)
                for i in strNum:
                    firstIdx += 1
                    chars[firstIdx] = i
            if chars[secondIdx] != curOne and firstIdx < len(chars)-1:
                firstIdx += 1
                numOfChar = 1
                curOne = chars[secondIdx]
                chars[firstIdx] = curOne
        secondIdx += 1
    return firstIdx+1


# print(compress("abc"))


def calcCost(x, y, a, b):
    return abs(x - a) + abs(y - b)


def minizeCost(numPeople, x, y):
    xx = []
    yy = []
    ans = 0
    for i in range(len(numPeople)):
        count = numPeople[i]
        count -= 1
        # while count:
        xx.append(x[i])
        yy.append(y[i])

    xx.sort()
    yy.sort()
    print(xx)
    print(yy)

    mx = xx[int(len(xx) / 2)]
    my = yy[int(len(yy) / 2)]

    for i in range(len(numPeople)):
        ans += numPeople[i] * calcCost(mx, x[i], y[i])

    return ans


print(minizeCost([1, 1], [1, 3], [1, 1]))

def memoizedAddTo8():
    cache = {}
    def AddTo80(n):
        if n in cache:
            return cache[n]
        else:
            print("Long time")
            cache[n] = n + 8
            return cache[n]
    return AddTo80


# memoized = memoizedAddTo8()
# print(memoized(10))
# print(memoized(10))
# print(memoized(10))

# Fibonacci Recursion
# global calculation
# calculation = 0

def fibonacciRecursive(n):
    calculation = 0
    if n < 2:
        # print (n)
        return n
    calculation += 1
    # print(calculation)
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciRecursiveMaster():
    cache = {}
    def calculateFib(n):
        if n in cache:
            return cache[n]
        else: 
            if n < 2:
                return n
            else:
                cache[n] = calculateFib(n-1) + calculateFib(n-2)
                return cache[n]
    return calculateFib

def fibonacciBottomUpDp(n):
    answer = [0,1]
    i = 2
    while i <= n:
        answer.append(answer[i-2] + answer[i-1])
        i += 1
    return answer.pop()



fasterFib = fibonacciRecursiveMaster()
print('fast ', fasterFib(100))
print('DP2', fibonacciBottomUpDp(100))
# print('slow', fibonacciRecursive(100))
# print(calculation)
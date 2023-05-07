def fibonacciIterative(n):
    arr = [0,1]
    i = 2
    while i < n+1:
        arr.append(arr[i-2] + arr[i-1])
        i += 1
    return arr[n]


# print(fibonacciIterative(43))


def fibonacciRecursive(n):
    if n < 2:
        print (n)
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)

def fibonacciRecursive2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacciRecursive2(n-1) + fibonacciRecursive2(n-2)
                    # 1                           0

print(fibonacciRecursive2(4))

def add(num0, num1):
    if num0 == 0:
        return num1
    return add(num1, num0-1) + 1

print(add(5,2))
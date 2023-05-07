def simpleRecursion(value):
    if value == 0:
        print("Blast Off!")
        return
    else:
        print(value)
        value = value - 1
        simpleRecursion(value)


# print(simpleRecursion(5))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 5

for i in range(0, n):
    print(fibonacci(i), end=" ")

def findFactorialRecursive(number):
    if number <= 2:
        return 2
    return number * findFactorialRecursive(number-1)

def findFactorialIterative(number):
    answer = 1
    if number == 2:
        answer = 2
    i = 2
    while i <= number:
        answer = answer * i
        i += 1
        print(answer)
    return answer


print(findFactorialIterative(5))
print(findFactorialRecursive(5))
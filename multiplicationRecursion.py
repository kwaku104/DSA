def multiplication(num0, num1):
    if num0 == 0 or num1 == 0:
        return 0
    return multiplication(num0, num1 - 1) + num0

# print(multiplication(7,6))

def division(num0, num1):
    if num0 == 0:
        return 0
    return division(num0 - 1, num1)

print(division(10 ,5))

# 7 + (7, 5)
# 7 + (7, 4)
# 7 + (7, 3)
# 7 + (7, 2)
# 7 + (7, 1)
# 7 + 0
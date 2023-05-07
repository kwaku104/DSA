numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def bubbleSort(numbers):
    for i in range(0, len(numbers)-1):
        for j in range(0, len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp



# bubbleSort(numbers)
# print(numbers)

def selectionSort(numbers):
    for i in range(0, len(numbers)-1):
        for j in range(0, len(numbers)-1):
            if numbers[j+1] < numbers[j]:
                temp = numbers[j+1]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp


selectionSort(numbers)
print(numbers)

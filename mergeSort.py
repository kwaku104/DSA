numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def mergeSort(array):
    if len(array) == 1:
        return array
    return mergeSort(
        mergeSort(left),
        mergeSort(right)
    )

def merge(left, right):
    pass


answer = mergeSort(numbers)
print(answer)
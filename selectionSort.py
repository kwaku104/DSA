numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selectionSort(numbers):
    length = len(numbers)
    for i in range(0, length-1):
        _min = i
        for j in range(i+1, length):
            if numbers[j] < numbers[_min]:
                # update minimum if current is lower than what we previously had
                _min = j
        if _min != i:
            numbers[i], numbers[_min] = numbers[_min], numbers[i]
    print(f'First selection sort {numbers}')


def selectionSort2(arr):
    for i in range(len(arr)):
        _min = i
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                _min = j

    arr[i], arr[_min] = arr[_min], arr[i]
    print(f'Second selection sort {arr}')


if __name__ == '__main__':
    selectionSort(numbers)
    selectionSort2(numbers)

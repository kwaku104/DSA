numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertionSort(numbers):
    length = len(numbers)
    for i in range(1, length):
        for j in range(i-1, 0, -1):
            if numbers[j] > numbers[j+1]:
                # update minimum if current is lower than what we previously had
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            else:
                break


def insertionSort2(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break

# Error needs to be corrected


def insertionSort3(A):
    for i in range(1, len(A)):
        curNum = A[i]
        for j in range(i-1, 0, -1):
            if A[j] > curNum:
                A[j+1] = A[j]
            else:
                A[j+1] = curNum
                break


# insertionSort3(numbers)
# print(numbers)


def insertionSortFinal(the_list):

    # For each item in the input list
    for index in range(len(the_list)):

        # Shift it to the left until it's in the right spot
        while index > 0 and the_list[index - 1] >= the_list[index]:
            the_list[index], the_list[index -
                                      1] = the_list[index - 1], the_list[index]
            index -= 1
            print(index)
    print(the_list)


if __name__ == '__main__':
    insertionSortFinal(numbers)

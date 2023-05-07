def mergeSortedArrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    mergedList = []
    array1Item = arr1[0]
    array2Item = arr2[0]
    i = 1
    j = 1
    while i < len(arr1) or j < len(arr2):
        if not array2Item or array1Item < array2Item:
            print(array1Item, array2Item)
            mergedList.append(array1Item)
            array1Item = arr1[i]
            i += 1
        else:
            mergedList.append(array2Item)
            array2Item = arr2[j]
            j += 1
            print(array1Item, array2Item)
    return mergedList


print(mergeSortedArrays([0,3,4,31], [4,6,30]))
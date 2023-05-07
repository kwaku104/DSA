# Naive
def hasPairWithSum(arr:list , _sum: int) -> bool:
    for i in arr:
        for j in arr:
            if i + j == _sum:
                return [arr.index(i), arr.index(j)]
    return False


print(hasPairWithSum([1,2,3,7], 8))













# Better
# def hasPairWithSum2(arr, _sum):
#     myList = []
#     for i in arr:
#         if i in myList:
#             return True
#         myList.append(_sum - i)
#     return False
    

# print(hasPairWithSum2([1,2,4,4], 8))

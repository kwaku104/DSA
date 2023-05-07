# import random
# def firstRC(arr):
#     recurring_list = []
#     i = 0
#     for i in arr:
#         while i <= len(arr):
#             recurring_list.append(i)
#             if arr[i] in recurring_list:
#                 return arr[i]
#             i += 1
#         return None


# print(firstRC([2,1,1,2,3,5,1,2,4]))

# keys = []
def firstRC2(arr):
    dictRC = {}
    for i in arr:
        if i in dictRC.values():
            return i
        else:
            dictRC = {random.random():i for i in arr}
    
    return dictRC


print(firstRC2([2,1,2,1,2,3,5,1,2,4]))

# def firstRC3(arr):
#     for i in arr:
#         for j in range(1,len(arr)):
#             if i == j:
#                 return i
#             else:
#                 return None


# print(firstRC3([]))
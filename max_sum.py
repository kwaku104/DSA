# def maxSubArray(nums):
#     temp = []                               
#     temp.append(nums[0])
#     for i in range(1,len(nums)):
#         r = max(nums[i],temp[i-1]+nums[i])
#         temp.append(r)
#         print(temp)
#     return max(temp)


# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# max(1)
# max(-3, -2)


def maxSubArray(nums):
    curr_max=nums[0]
    max_so_far=nums[0]
    for i in range(1,len(nums)):
        curr_max=max(nums[i],curr_max+nums[i]) # curr_max = max(1, -1)
        max_so_far=max(max_so_far,curr_max)
        # print(max_so_far)
    return max_so_far

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# Kadane's Algorithm
def Kadane(A):
    max_current = max_global = A[0]
    for i in range(1, len(A)-1):
        max_current = max(A[i], max_current + A[i])
        if max_current > max_global:
            max_global = max_current
    return max_global


print(Kadane([-2,1,-3,4,-1,2,1,-5,4]))



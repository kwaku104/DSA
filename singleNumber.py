from collections import defaultdict

def single_number(nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i


print(single_number([1,1,2,2,3,44,44,5,6]))
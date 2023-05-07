def moveZeroes(nums):
        pos = 0
        for i in range(len(nums)):
            print(pos, i)
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
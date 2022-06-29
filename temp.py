def largest_num(nums):
    """
    This print the largest number
    """
    maxnum = nums[0]
    for num in nums:
        if num > maxnum:
            #print(num)
            maxnum = num
            return maxnum
print(largest_num([1, 2, 3]))
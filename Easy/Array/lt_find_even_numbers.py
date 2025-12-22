def findNumbers(self, nums):
    """
       :type nums: List[int]
       :rtype: int
       """
    # 555,901,482,1771
    count_even = 0
    for i in range(len(nums)):
        len_i = len(str(nums[i]))
        if len_i % 2 == 0:
            count_even += 1
    return count_even

def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current_count_1s = 0
    max_count_1s = 0

    # [1,0,1,1,0,1]

    for i in range(len(nums)):
        if nums[i] == 1:
            current_count_1s += 1
            max_count_1s = max(current_count_1s, max_count_1s)
        else:
            current_count_1s = 0
    return max_count_1s

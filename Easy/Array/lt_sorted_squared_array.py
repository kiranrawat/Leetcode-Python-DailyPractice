def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    nums.sort()

    return nums

    # brute force
    # time complexity - O(nlogn)
    # space complexity - O(1)

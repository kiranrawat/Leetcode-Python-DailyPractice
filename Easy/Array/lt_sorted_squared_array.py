def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # for i in range(len(nums)):
    #     nums[i] = nums[i] ** 2
    # nums.sort()

    # return nums

    # brute force
    # time complexity - O(nlogn)
    # space complexity - O(1)

    # optimal in O(n) time complexity

    # [-4,-1,2,3,10] [0,4,9,16,100]
    left = 0
    n = len(nums)
    right = n - 1
    answer = [0]*n
    p = n - 1
    while left <= right:
        if nums[left] ** 2 < nums[right] ** 2:
            answer[p] = nums[right] ** 2
            right -= 1
        else:
            answer[p] = nums[left] ** 2
            left += 1
        p -= 1
    return answer

    # time complexity - O(n)
    # space complexity - O(n)

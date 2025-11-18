class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        if low > high:
            return low


nums = [4, 6, 8, 10, 11]
target = 12
s = Solution()
print(s.searchInsert(nums, target))

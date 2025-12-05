class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 1
        for right in range(1, len(nums)):  # 0
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1
        return left

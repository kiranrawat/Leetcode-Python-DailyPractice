class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        unique_elements = set(nums)
        if len(unique_elements) < len(nums):
            return True
        else:
            return False

# time complexity - O(n)
# space complexity - O(n)

# Input: nums = [1, 2, 3, 3]
# Output: true

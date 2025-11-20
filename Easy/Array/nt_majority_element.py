class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        len_nums = len(nums)
        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] = count_dict[nums[i]] + 1
            else:
                count_dict[nums[i]] = 1
        for i in count_dict.keys():
            if count_dict[i] > (len_nums/2):
                return i


# Time complexity - O(n+m)
# Space Complexity - O(m)

# Input: nums = [5,5,1,1,1,5,5]
# Output: 5

# Can we solve it in linear time and in O(1) space?

from collections import defaultdict


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count_dict = {}
#         len_nums = len(nums)
#         for i in range(len(nums)):
#             if nums[i] in count_dict:
#                 count_dict[nums[i]] = count_dict[nums[i]] + 1
#             else:
#                 count_dict[nums[i]] = 1
#         for i in count_dict.keys():
#             if count_dict[i] > (len_nums/2):
#                 return i


# Time complexity - O(n+m)
# Space Complexity - O(m)

# Input: nums = [5,5,1,1,1,5,5]
# Output: 5


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]

# Time complexity - O(nlogn)
# Space Complexity - O(1) or O(n) depending on sorting algo


# Can we solve it in linear time and in O(1) space?


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res

# Time complexity - O(n)
# Space Complexity - O(n)

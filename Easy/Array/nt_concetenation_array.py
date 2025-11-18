class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        # time complexity- O(2n), space complexity - O(n)
        # for i in range(len(nums)):
        #     nums.append(nums[i])
        # return nums
        # time complexity- O(n), space complexity - O(1)


# Input: nums = [1,4,1,2]

# Output: [1,4,1,2,1,4,1,2]

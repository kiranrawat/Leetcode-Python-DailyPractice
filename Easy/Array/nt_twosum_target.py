class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
        # time complexity - O(n^2), space complexity - O(n)

        # second solution
        # nums = [4,5,6] , target = 10
        index_dict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in index_dict:
                return [index_dict[difference], i]
            index_dict[nums[i]] = i
        # time complexity - O(n), space complexity - O(n)

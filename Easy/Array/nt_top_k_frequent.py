def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count_dict = {}
    for i in range(len(nums)):
        count_dict[nums[i]] = count_dict.get(nums[i], 0) + 1
    sorted_dict = {k: v for k, v in sorted(
        count_dict.items(), key=lambda item: item[1])}
    return list(sorted_dict.keys())[-k:]

# time complexity - O(M + NlogN), space complexity - O(N) where N is the unique number of elements in nums

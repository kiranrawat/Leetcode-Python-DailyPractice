def search(self, nums: List[int], target: int) -> int:
    # nums = [-1,0,2,4,6,8], target = 4
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# time complexity - O(logn), space complexity - O(1)

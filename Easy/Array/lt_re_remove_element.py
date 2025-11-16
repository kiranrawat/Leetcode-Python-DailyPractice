class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # nums= [0,1,2,2,3,0,4,2], val =2, nums = [[0,1,3,0,4]]
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

            # change the elements in such a way that first K elemnts are not equal to val
            # return the K.
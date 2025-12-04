class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start pointer
        last = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[last] = nums2[p2]
                p2 -= 1
            else:
                nums1[last] = nums1[p1]
                p1 -= 1
            last -= 1
        while p2 >= 0:
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1

    #     m= 4, n = 2, last=5, p1=3,p2=1
    #     [10,20,20,40,0,0]
    #     [100,200]

    #     40 < 200: true:
    #    [10,20,20,40,0,200] [100]
    #     p2 =0 , last = 4
    #     p1= 3

    #     40 < 100: true

    # [10,20,20,40,100,200]
    # p2 = -1,last = 3
    # p1 = 3

    #     [10,20,20,40,0,0]
    #     [1,2]

    #     last = 5, p1=3, p2=1
    #     40< 2 : False

    #     [10,20,20,40,0,40] [1,2]
    #     p1 = 2, last = 4, p2=1

    #     20< 2: False

    #     [10,20,20,40,20,40]  [1,2]

    #     p1 = 1, last = 3, p2=1

    #     20 < 2:
    #   [10,20,20,20,20,40]  [1,2]
    #     p1 = 0, last =2, p2 = 1

    #   [10,20,10,20,20,40]  [1,2]

    #   p1 = -1, last = 1, p2 = 1

    #   while p2 >= 0:
    #     nums1[last] = nums2[p2]
    #     p2 -= 1
    #     last -= 1

    # [10,2,10,20,20,40] , p2 = 0, last = 0
    # [1,2,10,20,20,40] , p2 = -1, last = -1

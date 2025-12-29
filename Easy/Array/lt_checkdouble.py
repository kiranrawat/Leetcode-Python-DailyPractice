def checkIfExist(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    seen = set()

    for element in arr:
        if element * 2 in seen:
            return True
        if element % 2 == 0 and element // 2 in seen:
            return True
        seen.add(element)
    return False

    # [10,2,5,3]

    # time complexity - O(n)
    # space complexity - O(n)

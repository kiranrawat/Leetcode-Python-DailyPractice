def duplicateZeros(self, arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    n = len(arr)
    i = 0

    while i < n:
        if arr[i] == 0:
            # Shift elements right
            for j in range(n - 1, i, -1):
                arr[j] = arr[j - 1]
            i += 1  # Skip the duplicated zero
        i += 1

# time complexity - O(n^2)
# space complexity - O(1)

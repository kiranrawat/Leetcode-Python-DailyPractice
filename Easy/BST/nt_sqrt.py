def mySqrt(self, x: int) -> int:
    low = 0
    high = x

    while low <= high:
        mid = low + ((high - low) // 2)  # never overflow
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            high = mid - 1
        else:
            low = mid + 1

    if low > high:
        return high


# time complexity - O(logn)
# space complexity - O(1)


# another solution (slight different)

def mySqrt(self, x: int) -> int:
    low = 0
    high = x
    res = 0

    while low <= high:
        mid = low + ((high - low) // 2)  # never overflow
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            high = mid - 1
        else:
            low = mid + 1
            res = mid

    return res

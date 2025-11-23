def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # solution 1
    # counter = 0
    # i = len(s)-1
    # for i in range(len(s)-1, -1, -1):
    #     if counter <= i:
    #         var = s[counter]
    #         s[counter] = s[i]
    #         s[i] = var
    #         counter+=1

    # solution 2
    i = 0
    while i <= ((len(s)-1)//2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        i += 1

    # solution 3
    # counter = 0
    # i = len(s)-1
    # while counter <= i:
    #     s[counter], s[i] = s[i], s[counter]
    #     counter += 1
    #     i -= 1

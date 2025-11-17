class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # haystack = "sadbbutsad"
        # needle = "but", 3 letters
        # check if 0th index has s, if not, go to next,
        # first position has s or not, if yes, check if ad followed the s
        if needle not in haystack:
            return -1
        len_needle = len(needle)
        for i in range(len(haystack)):  # 0,......,4
            if haystack[i: i+len_needle] == needle:
                return i

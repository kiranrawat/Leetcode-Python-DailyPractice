class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return len(s.split()[-1])
        count = 0
        rev = s[::-1]
        rev = rev.strip()
        for ch in rev:
            if ch == ' ':
                break
            else:
                count += 1
        return count

        # time complexity => O(n)
        # space complexity => o(1)


s = "hello world     example "
s = Solution()
print(s.lengthOfLastWord(s))

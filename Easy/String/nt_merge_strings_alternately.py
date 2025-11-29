class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        if len(word1) < len(word2):
            len_w = len(word1)
            remaning_str = word2[len_w:]
        else:
            len_w = len(word2)
            remaning_str = word1[len_w:]

        for i in range(len_w):
            res += word1[i]
            res += word2[i]

        return res+remaning_str

# time complexity - O(n)
# space complexity - O(n)


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        res = []
        i = j = 0
        while i < n or j < m:
            if i < n:
                res.append(word1[i])
            if j < m:
                res.append(word2[j])
            i += 1
            j += 1

        return "".join(res)

# time complexity - O(n + m)
# space complexity - O(n + m)

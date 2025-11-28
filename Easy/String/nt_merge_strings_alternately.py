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

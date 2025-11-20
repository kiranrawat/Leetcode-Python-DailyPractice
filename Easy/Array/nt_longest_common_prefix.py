class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs = ["bat","bag","bank","band"]
        # lcp = ""
        # if strs:
        #     # first_letter = strs[0][0]
        #     first_string = strs[0]
        # for char in first_string: #ba
        #     new_char = lcp + char
        #     for i, element in enumerate(strs):
        #         # print(element.startswith(new_char))
        #         if not element.startswith(new_char):
        #             return(lcp)
        #         elif (i == (len(strs) - 1)):
        #             lcp = new_char
        # return lcp

        prefix = strs[0]  # ["neet", "feet"]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix

# time complexity- O(m*n)
# space complexity - O(1)

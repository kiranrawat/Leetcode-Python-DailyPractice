class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t = {}
        count_s = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        return count_s == count_t

# time complexity - O(n + m) given length of s is n and length of t is m
# space complexity - O(1) since we have at most 26 different characters.


# Brute Force Approach

def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)
    # time complexity - O(nlogn) + O(mlogm), given n is the length of string s and m is the length of string t

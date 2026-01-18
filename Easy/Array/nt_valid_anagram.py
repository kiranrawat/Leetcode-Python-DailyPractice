class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        count_dict_1 = {}
        count_dict_2 = {}
        if len(s) != len(t):
            return False

        for letter_s in s:
            if letter_s in count_dict_1.keys():
                count_dict_1[letter_s] += 1
            else:
                count_dict_1[letter_s] = 1
        for letter_t in t:
            if letter_t in count_dict_2.keys():
                count_dict_2[letter_t] += 1
            else:
                count_dict_2[letter_t] = 1

        return count_dict_1 == count_dict_2

# time complexity - O(n + m) given length of s is n and length of t is m
# space complexity - O(1)


# Brute Force Approach

def isAnagram(self, s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)
    # time complexity - O(nlogn) + O(mlogm), given n is the length of string s and m is the length of string t

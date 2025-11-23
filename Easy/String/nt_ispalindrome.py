import re


def isPalindrome(self, s: str) -> bool:
    alphanum_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    i = 0
    while i <= (len(alphanum_s)//2):
        if alphanum_s[i] == alphanum_s[len(alphanum_s) - 1 - i]:
            i += 1
        else:
            return False

    if i > len(alphanum_s)//2:
        return True

# time complexity - O(n)
# space complexity - O(n)
# failed at submission, index out of range

# Can be solved in O(1) space complexity by using two-pointer approach.


def isPalindrome(self, s: str) -> bool:

    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

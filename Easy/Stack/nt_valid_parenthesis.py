def isValid(self, s: str) -> bool:
    stack = []
    open_to_close = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in open_to_close:
            if stack and stack[-1] == open_to_close[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

# time complexity - O(n)
# space complexity - O(n)


# brute force approach
def isValid(self, s: str) -> bool:
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')

    return s == ''

# time complexity - O(n^2)
# space complexity - O(n)

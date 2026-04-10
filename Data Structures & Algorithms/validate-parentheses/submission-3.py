class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(':')',
            '[':']',
            '{':'}',
        }
        for c in s:
            if c in mapping:
                stack.append(c)
            elif not stack or c != mapping[stack.pop()]:
                return False
        return True
